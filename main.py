# Main Method for Google Scraper of Tickers
import config
from GoogleScraper.googlescraper import *
from GoogleScraper.tickerparser import *
from GoogleScraper.configexporter import *

def main():
    print("Hello World!")
    generateTickersByYear(2016)
    generateTickerInterest()
    exportConfig()
    graph()

if __name__ == "__main__":
    main()