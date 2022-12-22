# Main Method for Google Scraper of Tickers
import config
from GoogleScraper.googlescraper import *
from GoogleScraper.tickerparser import *
from StockPicker.configexporter import *
from StockPicker.portfolioPicker import *
from NYTScraper.MainNYT import *
from NYTScraper.cohereTest import *

def main():
    print("Hello World!")
    

    generateTickersByYear(2016)
    generateGoogScore()
    graph()

    # generateArticleText()
    sumScore()
    #generateNYTScores()
    #print(config.NYTScores)
    pickStocks()
    printPortfolio()
    # exportConfig()

if __name__ == "__main__":
    main()