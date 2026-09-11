# Crypto Funding-Rate Arbitrage Scanner v1.0
A ready-to-use Python tool that scans Binance perpetual futures in real time and tells you which pairs currently pay you to hold a hedged (spot + perpetual) position.

## What you get
- crypto_analysis.py -- the scanner (MIT-licensed, modify freely)
- This guide

## Quick start
1. Install Python 3.10+ from python.org
2. pip install ccxt
3. python crypto_analysis.py

## Useful options
- python crypto_analysis.py --symbols BTC/USDT ETH/USDT --csv results.csv
- python crypto_analysis.py --min-annualized 10   (only show >=10%/yr)

## How funding-rate arbitrage works
Perpetual futures pay a "funding rate" every 8 hours. When it is positive, shorts receive it; when negative, longs receive it. By holding spot and the opposite perpetual contract you are market-neutral and collect funding. The scanner outputs the current direction (SHORT_PERP / LONG_PERP), per-8h funding, and annualized yield. This is not risk-free: fees, liquidation of the leveraged leg, and funding flips matter. Start small.

Educational tool, not financial advice.
