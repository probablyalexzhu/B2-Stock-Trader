# Author: Alex Zhu
# Last Updated: Dec 19, 2022

import pandas as pd

yearToAnalyze = 2016
if(yearToAnalyze > 2016 or yearToAnalyze < 2008):
    raise Exception("Year not between 2008 and 2016")

# NYSE sheet has been pre-processed to only include NASDAQ 100 stocks that are also on the NYSE
df = pd.read_excel(open('Google Scraper/Tickers.xlsx', 'rb'), sheet_name='NYSE')
tickersUnfiltered = df["Ticker"]
NASDAQorNot = df[yearToAnalyze]
tickersFiltered = [] # Tickers in the NYSE from that year's NASDAQ100

for idx, x in enumerate(NASDAQorNot):
    if x:
        tickersFiltered.append(tickersUnfiltered[idx])

print("Year: " + str(yearToAnalyze) + "\tNumber of Tickers: " + str(len(tickersFiltered)))
print(tickersFiltered)