# Author: Alex Zhu
# Last Updated: Jan 7, 2023

import re
import config
from StockPicker.configexporter import *
from Backtester.getCloseData import *

def backtest():
    # import names of tickers and year to analyze
    file1 = open('TempFiles/Portfolio.txt', 'r')
    count = 0
    tickersToAnalyzeUnprocessed = []

    # Using for loop to get lines from portfolio text file
    for line in file1:
        count += 1
        if count > 1:
            tickersToAnalyzeUnprocessed.append(line)

    tickersToAnalyzeProcessed = [i[1:5] for i in tickersToAnalyzeUnprocessed]

    # retrieve year to analyze from json
    yearNumTickers = []
    with open('TempFiles/yearNumTickers.json') as json_file:
        yearNumTickersFile = json.load(json_file)
    yearNumTickers = json.loads(yearNumTickersFile)
    year = yearNumTickers[0]

    # set start and end dates
    buyStart = "2009-01-01"
    buyEnd =  "2009-01-02"
    sellStart = "2022-12-31"
    sellEnd = "2023-01-02"

    startAmount = getCloseData(buyStart, buyEnd, tickersToAnalyzeProcessed)
    endAmount = getCloseData(sellStart, sellEnd, tickersToAnalyzeProcessed)

    startPortfolioValue = 100000
    startPortfolioNumberOfHoldings = []

    # invest 10k into each stock pick
    for i in tickersToAnalyzeProcessed:
        startPortfolioNumberOfHoldings.append(10000 / startAmount.get(i)[0])

    idx = 0
    for i in tickersToAnalyzeProcessed:
        config.portfolioValue += startPortfolioNumberOfHoldings[idx] * endAmount.get(i)[0]
        
        config.portfolioResult.append(startPortfolioNumberOfHoldings[idx] * endAmount.get(i)[0])

        idx += 1

    exportPortfolioResults(tickersToAnalyzeProcessed)