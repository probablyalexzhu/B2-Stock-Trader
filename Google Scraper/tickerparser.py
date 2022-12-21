# Author: Alex Zhu
# Last Updated: Dec 19, 2022

import pandas as pd
import config

def generateTickersByYear(year):
    config.yearToAnalyze = year
    if(config.yearToAnalyze > 2016 or config.yearToAnalyze < 2008):
        raise Exception("Year not between 2008 and 2016")

    # NYSE sheet has been pre-processed to only include NASDAQ 100 stocks that are also on the NYSE
    df = pd.read_excel(open('Google Scraper/Tickers.xlsx', 'rb'), sheet_name='NYSE')
    tickersUnfiltered = df["Ticker"]
    NASDAQorNot = df[config.yearToAnalyze]

    for idx, x in enumerate(NASDAQorNot):
        if x:
            config.tickersFiltered.append("$" + tickersUnfiltered[idx])

    config.numTickers = len(config.tickersFiltered)
    print("Year: " + str(config.yearToAnalyze) + "\tNumber of Tickers: " + str(len(config.tickersFiltered)))
    print(config.tickersFiltered)