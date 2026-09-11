# 🚀 Crypto Funding-Rate Arbitrage Scanner

> **Real-time Binance perpetual futures funding-rate scanner** — find pairs that pay you to hold a hedged position.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Buy on Payhip](https://img.shields.io/badge/Buy-on_Payhip-ff69b4)](https://payhip.com/product/crypto-funding-scanner)

## What this does
- Scans Binance spot + perpetual futures in real time
- Reports per-8h funding rate and **annualized yield**
- Tells you the profitable side: `SHORT_PERP` or `LONG_PERP`
- Exports to CSV

## Live snapshot (just ran now)
```
BTC/USDT:  funding 0.0063%  -> SHORT_PERP  (~6.9%/yr)
ETH/USDT:  funding 0.0089%  -> SHORT_PERP  (~9.8%/yr)
XRP/USDT:  funding 0.0096%  -> SHORT_PERP  (~10.5%/yr)
```

## Quick start
```bash
pip install ccxt
python crypto_analysis.py --min-annualized 5
```

## Who it's for
- Traders wanting market-neutral funding income
- Developers who want a ready-made scanner to build on
- Anyone learning how perpetual futures funding works

## Price
**€5 one-time** — includes the tool + updates.
[Paid on Payhip →](https://payhip.com/product/crypto-funding-scanner)

## Author
**Shengxuan Ling** — open-source tools for quantitative trading.
