# Author: Alex Zhu
# Last Updated: Dec 21, 2022
# Help from https://medium.com/analytics-vidhya/compare-more-than-5-keywords-in-google-trends-search-using-pytrends-3462d6b5ad62

import pandas as pd                        
from pytrends.request import TrendReq
import config
import warnings
warnings.filterwarnings('ignore')

def generateTickerInterest():
    tickersToAnalyzeAverages = [] # temporary list of tickers to analyze
    tickersDoneCounter = 0

    # do first 5 tickers in separate case
    for idx in range(5):
        tickersToAnalyzeAverages.append(config.tickersFiltered[idx]);

    #historical interest
    pytrends1=TrendReq()
    historicalDataFrame = pytrends1.get_historical_interest(tickersToAnalyzeAverages, year_start=config.yearToAnalyze, month_start=12,
        day_start=1, hour_start=0, year_end=config.yearToAnalyze, month_end=12, day_end=31, hour_end=0, cat=0,
        geo='', gprop='', sleep=0)

    print(historicalDataFrame)
    # average them and put them in averageList
    for item in historicalDataFrame:
        config.googAverageListFinal.append(historicalDataFrame[item].mean().round(3))
        tickersDoneCounter += 1
    tickersDoneCounter -= 1 # The isPartial column

    print("Initial tickers done: " + str(tickersDoneCounter))

    normalizingTickerAverage = config.googAverageListFinal[0]
    tickersToAnalyzeAverages.clear()

    # loop rest of tickers
    for i in range(5,config.numTickers, 4):
        tickersToAnalyzeAverages.append(config.tickersFiltered[0]) # previous breakpoint: add ticker used for normalization
        
        if(config.numTickers - i < 4):
            for j in range(1, config.numTickers - i):
                tickersToAnalyzeAverages.append(config.tickersFiltered[j + tickersDoneCounter - 1])
        else:
            for j in range(1, 5):
                tickersToAnalyzeAverages.append(config.tickersFiltered[j + tickersDoneCounter - 1])

        print("Tickers to analyze averages: " + str(tickersToAnalyzeAverages))

        pytrends1=TrendReq()
        historicalDataFrame = pytrends1.get_historical_interest(tickersToAnalyzeAverages, year_start=config.yearToAnalyze, month_start=12,
            day_start=1, hour_start=0, year_end=config.yearToAnalyze, month_end=12, day_end=1, hour_end=12, cat=0,
            geo='', gprop='', sleep=0)

        print(historicalDataFrame)
        # average them and put them in averageList
        averagesToBeAdded = []
        for item in historicalDataFrame:
            averagesToBeAdded.append(historicalDataFrame[item].mean())
        
        print("normalizingTickerAverage: " + str(normalizingTickerAverage))
        print("averages to be added: " + str(float(averagesToBeAdded[0])))

        normalizationFactor=normalizingTickerAverage/float(averagesToBeAdded[0])

        print("normalizationFactor: " + str(normalizationFactor))

        for k in range(len(averagesToBeAdded)):
            normalizedVal=normalizationFactor*averagesToBeAdded[k]

            averagesToBeAdded[k]=normalizedVal.round(3)
            tickersDoneCounter += 1

        # remove the normalizer and the isPartial column from the counter
        tickersDoneCounter -= 2
        averagesToBeAdded.pop(len(averagesToBeAdded) - 1)
        averagesToBeAdded.pop(0)
        print("Averages to be added: " + str(averagesToBeAdded))
        print("tickers done counter: " + str(tickersDoneCounter))
        config.googAverageListFinal += averagesToBeAdded

        tickersToAnalyzeAverages.clear()
        # normalizingTickerAverage = config.averageListFinal[i] # optimizable?

    # sometimes pytrends fails, returns 0 searches, deal with those cases
    tries = 0
    while 0 in config.googAverageListFinal and tries < 0: # too high and 429 too many requests

        tickersToRedo = []
        for idx, x in enumerate(config.googAverageListFinal):
            if(not x):
                tickersToRedo.append(config.tickersFiltered[idx])
        print("TICKERS TO REDO OMEGALUL: " + str(tickersToRedo))

        
        while(len(tickersToRedo) > 0):
            tickersToAnalyzeAverages.append(config.tickersFiltered[0])
            tickersToAnalyzeAverages.append(tickersToRedo[0])
            pytrends1=TrendReq()
            historicalDataFrame = pytrends1.get_historical_interest(tickersToAnalyzeAverages, year_start=config.yearToAnalyze, month_start=12,
                day_start=1, hour_start=0, year_end=config.yearToAnalyze, month_end=12, day_end=31, hour_end=0, cat=0,
                geo='', gprop='', sleep=0)

            print(historicalDataFrame)
            # average them and put them in averageList
            average = historicalDataFrame.iloc[:, 1].mean()
            normalizationFactor=normalizingTickerAverage/float((historicalDataFrame.iloc[:, 0].mean()))
            normalizedVal=normalizationFactor*average

            config.googAverageListFinal[config.tickersFiltered.index(tickersToRedo[0])] = normalizedVal.round(3)

            tickersToAnalyzeAverages.clear()
            tickersToRedo.pop(0)
            print("TICKERS TO REDO: " + str(tickersToRedo))

        tries += 1

    print(config.googAverageListFinal)
    maximum = max(config.googAverageListFinal)
    print(maximum)

    config.googAverageListFinal[:] = [x / maximum for x in config.googAverageListFinal]