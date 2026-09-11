# -*- coding: utf-8 -*-
# Cryptocurrency Arbitrage Analysis Tool
import ccxt
import json
from datetime import datetime

class CryptoArbitrageAnalyzer:
    """Real-time crypto arbitrage analyzer using ccxt."""
    
    def __init__(self):
        self.exchange = ccxt.binance()
        self.exchange.load_markets()
    
    def get_spot_price(self, symbol):
        """Get current spot price."""
        try:
            ticker = self.exchange.fetch_ticker(symbol)
            return ticker["last"]
        except Exception as e:
            return None
    
    def get_funding_rate(self, symbol):
        """Get current funding rate for a perpetual contract."""
        try:
            funding = self.exchange.fetch_funding_rate(symbol)
            return funding.get("fundingRate", None)
        except Exception as e:
            return None
    
    def analyze(self, symbols=["BTC/USDT", "ETH/USDT"]):
        """Analyze symbols for arbitrage opportunities."""
        results = {}
        for symbol in symbols:
            spot = self.get_spot_price(symbol)
            perp_symbol = symbol.replace("/", "") + ":USDT"
            funding = self.get_funding_rate(perp_symbol)
            results[symbol] = {
                "spot_price": spot,
                "funding_rate": funding,
                "opportunity": "LONG" if funding and funding < 0 else ("SHORT" if funding and funding > 0 else "NEUTRAL"),
                "timestamp": datetime.utcnow().isoformat()
            }
        return results

if __name__ == "__main__":
    analyzer = CryptoArbitrageAnalyzer()
    result = analyzer.analyze()
    print(json.dumps(result, indent=2))

