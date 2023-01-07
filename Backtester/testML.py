import json
import yfinance as yf

# import names of tickers and year to analyze
localTickersFiltered = []
with open('TempFiles/tickersFiltered.json') as json_file:
    localTickersFilteredFile = json.load(json_file)
localTickersFiltered = json.loads(localTickersFilteredFile)

tickersWithoutSign = [i[1:] for i in localTickersFiltered]

yearNumTickers = []
with open('TempFiles/yearNumTickers.json') as json_file:
    yearNumTickersFile = json.load(json_file)
yearNumTickers = json.loads(yearNumTickersFile)
year = yearNumTickers[0]

def printCloseData(start, end, tickers):
    
    data = yf.download(
        tickers = tickers,
        start = start, 
        end = end,
        interval = "3mo",
    )
    print(data['Close'])