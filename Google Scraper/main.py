# Main Method for Google Scraper of Tickers
import config
from googlescraper import *
from tickerparser import *
from configexporter import *

def main():
    print("Hello World!")
    generateTickersByYear(2016)
    generateTickerInterest()
    exportConfig()
    graph()

if __name__ == "__main__":
    main()