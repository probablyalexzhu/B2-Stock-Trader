# B2 Stock Trader: Alternative Data Trading using Python, Google Trends, NYT Articles, and Cohere

## Description
The B2 stock trader is an application that uses Google Trends and Cohere sentiment analysis on NYT articles to pick a portfolio of stocks. It uses an algorithmic strategy of finding undervalued (low Google interest) but highly-rated (high NYT sentiment scores) stocks that others neglect looking at, because most people focus on popular but likely overvalued stocks. We were inspired by B2EMO, a groundmech salvage assist droid in Star Wars: Andor that looked through junkyards for valuable scrap. Similarly, we scrape the internet to find undervalued stocks.

We built this project to learn about sourcing and processing data ourselves for the purpose of alternative data trading, improve our abilities to work with libraries and APIs, and practice using Git and debugging projects; we succeeded at reaching that goal. The goal was not necessarily to create a safe portfolio that maximizes profit which would be useful in the real world. However, B2 was still highly successful in choosing profitable portfolios.

| ![image](https://user-images.githubusercontent.com/87958079/211218481-c3b136f9-3788-4bc7-a046-4bbe5a443c8c.png) |
|:--:| 
| ![image](https://user-images.githubusercontent.com/87958079/211218228-f35831f5-569a-48e0-bb28-bd4338d0f14e.png) |
| ![image](https://user-images.githubusercontent.com/87958079/211218549-5efe465e-63db-454d-8b48-c70afbcc5a72.png) |
| *The B2 portfolios beat the S&P 500 by a huge 1212% and 817%, respectively, between Jan 1, 2008 and Dec 31, 2022.* |

We tested starting from 2008, which is as far back as we could go to find a list of that year's Nasdaq-100 stocks. We used the Nasdaq-100 stocks as a starting point, then since we were trading on the NYSE, we reduced the 100 stocks to approximately 80 that were traded on the NYSE and not just the NASDAQ. From there, we implemented our two strategies to pick approximately 10 stocks to form our portfolio:

1. NYTScraper - long, high brand value companies: High brand value companies build up a better reputation increasing customer loyalty and employee retention. In the long run, these effects multiply themselves and lead the company to large potential for growth. In the NYTScraper, the pynytimes API is used to get headlines of articles containing a stock's name, then Cohere performs a sentiment analysis using custom training data to determine if the headlines are positive or negative. The scores are averaged out to generate a sentiment score.

2. GoogleScraper - long, low attention companies: While low volatility strategies have been around for a long time, using our improved technologies, there are better ways to measure low risk or low attention of investors to find undervalued companies. The premises of this strategy is that firstly, these stocks tend to be underpriced, and once the attention turns back towards them, their prices tend to increase. Secondly, these stocks are usually associated with lower risk. In the GoogleScraper, the pytrends API is used to get historical data from Google Trends of stock tickers. Stocks are compared, and those with low search volume receive a more favourable search score.

[insert block diagram here]

Once a final score that took the NYT and Google scores into account was generated for each stock, a portfolio was generated and backtested using the yfinance API. We tested more on 2010 and 2012, reaching profits of up to 633% and 648%, respectively.

What makes our project stand out is that we did all of it at no cost. Finance is largely gatekept; it costs money to gain access to historical stock data, SEO information, alternative data sources, financial advice, and more. We found creative ways to source the information we needed, such as using the Wayback Machine, albeit sometimes limited by API call limits and volume of available information.

## How to Install and Run

## How to Use
You will need to download pytrends, pynytimes, pandas, cohere, configparser, and yfinance. Create your own config.ini file in the NYTScraper folder with your own free API keys for pynytimes and Cohere. Then, run main.py in the main folder, passing in the year you want to analyze in generateTickersByYear(), and making sure all the functions are uncommented. Wait for API calls to finish, and the .json and .txt files should update with the chosen portfolio and results. It is set to parse the last month of the year's Google Trends data, and the full year's NYT articles. You can change these timeframes yourself in the respective files, at the cost of runtime and potentially reaching the API call limits.

## Challenges Faced

## Next Steps

## Credits
This project was co-created by Ryan Shen and Alex Zhu, with research and use of:
https://quantpedia.com/six-examples-of-trading-strategies-that-use-alternative-data/
https://medium.com/swlh/build-an-ai-stock-trading-bot-for-free-4a46bec2a18
https://web.archive.org/web/20160402172246/http://siblisresearch.com/data/historical-components-nasdaq 
https://medium.com/analytics-vidhya/compare-more-than-5-keywords-in-google-trends-search-using-pytrends-3462d6b5ad62
https://www.portfoliovisualizer.com/backtest-portfolio#analysisResults
