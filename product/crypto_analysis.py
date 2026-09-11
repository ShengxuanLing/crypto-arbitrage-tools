# -*- coding: utf-8 -*-
"""Crypto Funding-Rate Arbitrage Scanner v1.0
Requires: pip install ccxt
"""
import argparse, csv, json
from datetime import datetime, timezone
import ccxt

DEFAULT_SYMBOLS = ["BTC/USDT", "ETH/USDT", "BNB/USDT", "SOL/USDT", "XRP/USDT"]

class FundingRateScanner:
    def __init__(self):
        self.spot = ccxt.binance()
        self.perp = ccxt.binanceusdm()
        self.spot.load_markets(); self.perp.load_markets()

    def scan_symbol(self, symbol):
        spot_price = self.spot.fetch_ticker(symbol)["last"]
        perp_symbol = f"{symbol}:USDT"
        ticker = self.perp.fetch_ticker(perp_symbol)
        funding = self.perp.fetch_funding_rate(perp_symbol)
        rate = funding.get("fundingRate")
        basis_pct = (ticker["last"] / spot_price - 1) * 100 if spot_price else None
        if rate is None: direction = "UNKNOWN"
        elif rate > 0: direction = "SHORT_PERP"
        elif rate < 0: direction = "LONG_PERP"
        else: direction = "NEUTRAL"
        return {"symbol": symbol, "spot_price": spot_price, "perp_price": ticker["last"],
                "basis_pct": round(basis_pct, 4) if basis_pct is not None else None,
                "funding_rate": rate,
                "funding_pct": round(rate * 100, 4) if rate is not None else None,
                "annualized_pct": round(rate * 3 * 365 * 100, 2) if rate is not None else None,
                "strategy": direction,
                "timestamp": datetime.now(timezone.utc).isoformat()}

    def scan(self, symbols=DEFAULT_SYMBOLS):
        out = []
        for s in symbols:
            try: out.append(self.scan_symbol(s))
            except Exception as e: out.append({"symbol": s, "error": str(e)})
        return out

def main():
    p = argparse.ArgumentParser(description="Crypto funding-rate arbitrage scanner")
    p.add_argument("--symbols", nargs="+", default=DEFAULT_SYMBOLS)
    p.add_argument("--csv", help="Export results to CSV")
    p.add_argument("--min-annualized", type=float, default=0)
    args = p.parse_args()
    results = FundingRateScanner().scan(args.symbols)
    print(json.dumps(results, indent=2))
    actionable = [r for r in results if r.get("annualized_pct") is not None and abs(r["annualized_pct"]) >= args.min_annualized]
    if actionable:
        print(f"\n=== Opportunities (|annualized| >= {args.min_annualized}%) ===")
        for r in sorted(actionable, key=lambda x: -abs(x["annualized_pct"])):
            print(f"  {r['symbol']}: funding {r['funding_pct']}% -> {r['strategy']} (~{r['annualized_pct']}%/yr)")
    if args.csv:
        keys = ["symbol","spot_price","perp_price","basis_pct","funding_rate","funding_pct","annualized_pct","strategy","timestamp"]
        with open(args.csv, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=keys, extrasaction="ignore"); w.writeheader(); w.writerows(results)
        print(f"Saved to {args.csv}")

if __name__ == "__main__":
    main()
