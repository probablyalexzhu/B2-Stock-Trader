# Main Method for Google Scraper of Tickers
import config
from GoogleScraper.googlescraper import *
from GoogleScraper.tickerparser import *
from StockPicker.configexporter import *
from StockPicker.stockPicker import *

def main():
    print("Hello World!")
    generateTickersByYear(2016)
    generateGoogScore()
    graph()

    # add command to generate and save NYTScores
    sumScore()
    pickStocks()
    createPortfolio()
    exportConfig()

if __name__ == "__main__":
    main()