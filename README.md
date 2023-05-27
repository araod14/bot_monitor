# bot_monitor
This script can monitor the next currency pairs:
["TRX/USDT",
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
