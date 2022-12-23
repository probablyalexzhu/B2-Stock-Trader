# Main Method for Google Scraper of Tickers
import config
from GoogleScraper.googlescraper import *
from GoogleScraper.tickerparser import *
from StockPicker.configexporter import *
from StockPicker.portfolioPicker import *
from NYTScraper.mainNYT import *
from NYTScraper.cohereSentiment import *

def main():
    # Should be run in this order: generate tickers, generate search scores, generate article text, generate nytscores, sum score, pick stocks, print portfolio
    print("Hello World!")
    # generateTickersByYear(2015)
    # generateSearchScores()
    # graph()
    # generateArticleText()
    generateNYTScores()
    # sumScore()
    # pickStocks()
    # printPortfolio()

if __name__ == "__main__":
    main()