# Main Method for B2
# Author: Ryan Shen and Alex Zhu
# Last Updated: Jan 7, 2023
import config
from GoogleScraper.googlescraper import *
from GoogleScraper.tickerparser import *
from StockPicker.configexporter import *
from StockPicker.portfolioPicker import *
from NYTScraper.mainNYT import *
from NYTScraper.cohereSentiment import *
from Backtester.mainBacktester import *

# Should be run in this order: generate tickers, generate search scores, generate article text,
# generate nytscores, sum score, pick stocks, print portfolio, backtest
def main():
    # print("running")
    # generateTickersByYear(2008)
    # generateSearchScores()
    # graph()
    # generateArticleText()
    # generateNYTScores()
    # sumScore()
    # pickStocks()
    # printPortfolio()
    backtest()

if __name__ == "__main__":
    main()