# Author: Alex Zhu
# Last Updated: Dec 21, 2022
# Help from https://medium.com/analytics-vidhya/compare-more-than-5-keywords-in-google-trends-search-using-pytrends-3462d6b5ad62

import pandas as pd                        
from pytrends.request import TrendReq
from StockPicker.configexporter import *
import config
import warnings
warnings.filterwarnings('ignore')
import json

def generateSearchScores():
    localTickersFiltered = []
    with open('TempFiles/tickersFiltered.json') as json_file:
        localTickersFilteredFile = json.load(json_file)
    localTickersFiltered = json.loads(localTickersFilteredFile)

    yearNumTickers = []
    with open('TempFiles/yearNumTickers.json') as json_file:
        yearNumTickersFile = json.load(json_file)
    yearNumTickers = json.loads(yearNumTickersFile)
    year = yearNumTickers[0]
    numTickers = yearNumTickers[1]

    tickersToAnalyzeAverages = [] # temporary list of tickers to analyze
    tickersDoneCounter = 0

    # do first 5 tickers in separate case
    for idx in range(5):
        tickersToAnalyzeAverages.append(localTickersFiltered[idx]);

    #historical interest
    pytrends1=TrendReq()
    historicalDataFrame = pytrends1.get_historical_interest(tickersToAnalyzeAverages, year_start=year, month_start=12,
        day_start=1, hour_start=0, year_end=year, month_end=12, day_end=31, hour_end=0, cat=0,
        geo='', gprop='', sleep=0)

    # print(historicalDataFrame)
    # average them and put them in averageList
    for item in historicalDataFrame:
        config.searchScores.append(historicalDataFrame[item].mean().round(3))
        tickersDoneCounter += 1
    tickersDoneCounter -= 1 # The isPartial column

    print("Initial tickers done: " + str(tickersDoneCounter))

    normalizingTickerAverage = config.searchScores[0]
    tickersToAnalyzeAverages.clear()

    # loop rest of tickers
    for i in range(5,numTickers, 4):
        tickersToAnalyzeAverages.append(localTickersFiltered[0]) # previous breakpoint: add ticker used for normalization
        
        if(numTickers - i < 4):
            for j in range(1, numTickers - i):
                tickersToAnalyzeAverages.append(localTickersFiltered[j + tickersDoneCounter - 1])
        else:
            for j in range(1, 5):
                tickersToAnalyzeAverages.append(localTickersFiltered[j + tickersDoneCounter - 1])

        print("Tickers to analyze averages: " + str(tickersToAnalyzeAverages))

        pytrends1=TrendReq()
        historicalDataFrame = pytrends1.get_historical_interest(tickersToAnalyzeAverages, year_start=year, month_start=12,
            day_start=1, hour_start=0, year_end=year, month_end=12, day_end=31, hour_end=0, cat=0,
            geo='', gprop='', sleep=0)

        # print(historicalDataFrame)
        # average them and put them in averageList
        averagesToBeAdded = []
        for item in historicalDataFrame:
            averagesToBeAdded.append(historicalDataFrame[item].mean())
        
        # print("normalizingTickerAverage: " + str(normalizingTickerAverage))
        # print("averages to be added: " + str(float(averagesToBeAdded[0])))

        normalizationFactor=normalizingTickerAverage/float(averagesToBeAdded[0])

        # print("normalizationFactor: " + str(normalizationFactor))

        for k in range(len(averagesToBeAdded)):
            normalizedVal=normalizationFactor*averagesToBeAdded[k]

            averagesToBeAdded[k]=normalizedVal.round(3)
            tickersDoneCounter += 1

        # remove the normalizer and the isPartial column from the counter
        tickersDoneCounter -= 2
        averagesToBeAdded.pop(len(averagesToBeAdded) - 1)
        averagesToBeAdded.pop(0)
        # print("Averages to be added: " + str(averagesToBeAdded))
        print("tickers done: " + str(tickersDoneCounter))
        config.searchScores += averagesToBeAdded

        tickersToAnalyzeAverages.clear()
        # normalizingTickerAverage = config.averageListFinal[i] # optimizable?

    # sometimes pytrends fails, returns 0 searches, deal with those cases
    tries = 0
    while 0 in config.searchScores and tries < 0: # too high and 429 too many requests

        tickersToRedo = []
        for idx, x in enumerate(config.searchScores):
            if(not x):
                tickersToRedo.append(localTickersFiltered[idx])
        print("Tickers to Try Again: " + str(tickersToRedo))

        while(len(tickersToRedo) > 1):
            tickersToAnalyzeAverages.append(localTickersFiltered[0])
            tickersToAnalyzeAverages.append(tickersToRedo[0])
            pytrends1=TrendReq()
            historicalDataFrame = pytrends1.get_historical_interest(tickersToAnalyzeAverages, year_start=year, month_start=10,
                day_start=1, hour_start=0, year_end=year, month_end=12, day_end=31, hour_end=0, cat=0,
                geo='', gprop='', sleep=0)

            # print(historicalDataFrame)
            # average them and put them in averageList
            average = historicalDataFrame.iloc[:, 1].mean()
            normalizationFactor=normalizingTickerAverage/float((historicalDataFrame.iloc[:, 0].mean()))
            normalizedVal=normalizationFactor*average

            config.searchScores[localTickersFiltered.index(tickersToRedo[0])] = normalizedVal.round(3)

            tickersToAnalyzeAverages.clear()
            tickersToRedo.pop(0)
            print("Tickers to Try Again: " + str(tickersToRedo))

        tries += 1

    # print(config.searchScores)
    maximum = max(config.searchScores)
    # print(maximum)
    config.searchScores[:] = [x / maximum for x in config.searchScores]
    exportSearchScores()