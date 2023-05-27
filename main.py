"""
This script can monitor the next currency pairs:
[            "TRX/USDT",
            "UNI/USDT",
            "LINK/USDT",
            "XLM/USDT",
            "FIL/USDT",
            "ALGO/USDT",
            "VET/USDT",
            "MANA/USDT",
            "EOS/USDT",
            "AAVE/USDT"           
        ] 
in the time frames: 1-hour; 24 hours; and 3, daily.

when the price touches the X EMA on the 1-hour time frame and the 4-hour X EMA aligns with the 1-hour X EMA, an alert should be generated. The same applies to the 4-hour and daily time frames.
"""
import os
import numpy as np
from binance.client import Client
from talib import EMA
#conda install -c conda-forge ta-lib

# Set up Binance API client
api_key = os.environ.get('BINANCE_API_KEY')
api_secret = os.environ.get('BINANCE_API_SECRET')
client = Client(api_key, api_secret)

# List of currency pairs to monitor
pairs = ["TRXUSDT", "UNIUSDT", "LINKUSDT", "XLMUSDT", "FILUSDT", "ALGOUSDT", "VETUSDT", "MANAUSDT", "EOSUSDT", "AAVEUSDT"]

# List of time frames to monitor
timeframes = ["1h", "4h", "1d"]

# Define EMA length
ema_length = 20

# Loop through each currency pair and time frame
for pair in pairs:
    for tf in timeframes:
        # Retrieve historical klines data for the current time frame
        klines = client.get_historical_klines(pair, tf, "1 day ago UTC")
        
        # Extract close prices from klines data
        close_prices = [float(kline[4]) for kline in klines]
        
        # Calculate EMA for the current time frame
        ema = EMA(np.array(close_prices), timeperiod=ema_length)
        
        # Calculate EMA for the next time frame
        next_tf = "4h" if tf == "1h" else "1d"
        next_klines = client.get_historical_klines(pair, next_tf, "1 day ago UTC")
        next_close_prices = [float(kline[4]) for kline in next_klines]
        next_ema = EMA(np.array(next_close_prices), timeperiod=ema_length)
        
        # Check if the current EMA is above the next EMA
        if ema[-1] > next_ema[-1]:
            # Generate an alert
            alert_message = f"EMA cross alert: {pair} on the {tf} time frame"
            print(alert_message)