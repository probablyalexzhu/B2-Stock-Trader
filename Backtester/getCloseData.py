# Author: Alex Zhu
# Last Updated: Jan 6, 2023

import json
import yfinance as yf

def getCloseData(start, end, tickers):
    
    data = yf.download(
        tickers = tickers,
        start = start, 
        end = end,
        interval = "3mo",
    )
    return data['Close']