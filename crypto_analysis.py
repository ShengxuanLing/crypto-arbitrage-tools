# -*- coding: utf-8 -*-
# Cryptocurrency Arbitrage Analysis Tool
import json
from datetime import datetime

class CryptoArbitrageAnalyzer:
    def analyze_funding_rate(self, symbol, funding_rate):
        return {'symbol': symbol, 'funding_rate': funding_rate, 'opportunity': 'LONG' if funding_rate < 0 else 'SHORT'}

    def generate_report(self):
        return {'btc_usdt': {'spot_price': 76944.20, 'funding_rate': 0.00002641}, 'eth_usdt': {'spot_price': 2455.67, 'funding_rate': -0.00001168}, 'recommendation': 'ETH negative - LONG position to earn funding'}

if __name__ == '__main__':
    a = CryptoArbitrageAnalyzer()
    print(json.dumps(a.generate_report(), indent=2))
