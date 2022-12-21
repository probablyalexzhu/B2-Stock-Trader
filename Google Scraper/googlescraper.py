# Author: Alex Zhu
# Last Updated: Dec 20, 2022
# Help from https://medium.com/analytics-vidhya/compare-more-than-5-keywords-in-google-trends-search-using-pytrends-3462d6b5ad62

import pandas as pd                        
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import numpy as np
import config
import warnings
warnings.filterwarnings('ignore')

def generateTickerInterest():
    averageListFinal = []
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
        averageListFinal.append(historicalDataFrame[item].mean().round(2))
        tickersDoneCounter += 1
    tickersDoneCounter -= 1 # The isPartial column

    print("Initial tickers done: " + str(tickersDoneCounter))

    normalizingTickerAverage = averageListFinal[0]
    tickersToAnalyzeAverages.clear()

    # loop rest of tickers
    for i in range(5,config.numTickers, 4):
        tickersToAnalyzeAverages.append(config.tickersFiltered[0]) # previous breakpoint: add previous ticker used for normalization
        
        if(config.numTickers - i < 4):
            for j in range(1, config.numTickers - i):
                tickersToAnalyzeAverages.append(config.tickersFiltered[(j - 1) + tickersDoneCounter - 1])
        else:
            for j in range(1, 5):
                tickersToAnalyzeAverages.append(config.tickersFiltered[(j - 1) + tickersDoneCounter - 1])

        print("Tickers to analyze averages: " + str(tickersToAnalyzeAverages))

        pytrends1=TrendReq()
        historicalDataFrame = pytrends1.get_historical_interest(tickersToAnalyzeAverages, year_start=config.yearToAnalyze, month_start=12,
            day_start=1, hour_start=0, year_end=config.yearToAnalyze, month_end=12, day_end=31, hour_end=0, cat=0,
            geo='', gprop='', sleep=0)

        print(historicalDataFrame)
        # average them and put them in averageList
        averagesToBeAdded = []
        for item in historicalDataFrame:
            averagesToBeAdded.append(historicalDataFrame[item].mean().round(2))
        
        normalizationFactor=normalizingTickerAverage/averagesToBeAdded[0]

        for k in range(len(averagesToBeAdded)):
            normalisedVal=normalizationFactor*averagesToBeAdded[k]
            averagesToBeAdded[k]=normalisedVal.round(2)
            tickersDoneCounter += 1

        # remove the normalizer and the isPartial column from the counter
        tickersDoneCounter -= 2
        averagesToBeAdded.pop(len(averagesToBeAdded) - 1)
        averagesToBeAdded.pop(0)
        print("Averages to be added: " + str(averagesToBeAdded))
        print("tickers done counter: " + str(tickersDoneCounter))
        averageListFinal += averagesToBeAdded

        tickersToAnalyzeAverages.clear()
        # normalizingTickerAverage = averageListFinal[i] # optimizable?

    # GrAPH it
    y_pos=np.arange(len(config.tickersFiltered))
    plt.barh(y_pos,averageListFinal,align='center',alpha=0.5)
    plt.yticks(y_pos,config.tickersFiltered)
    plt.xlabel('Average search density')
    plt.show()