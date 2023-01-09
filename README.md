# B2 Stock Trader: Alternative Data Trading using Python, Google Trends, NYT Articles, and Cohere

## Description
Read our Medium article here: 

The B2 stock trader is an application that uses Google Trends and Cohere sentiment analysis on NYT articles to pick a portfolio of stocks. It uses an algorithmic strategy of finding undervalued (low Google interest) but highly-rated (high NYT sentiment scores) stocks that others neglect looking at, because most people focus on popular but likely overvalued stocks. We were inspired by B2EMO, a groundmech salvage assist droid in Star Wars: Andor that looked through junkyards for valuable scrap. Similarly, we scrape the internet to find undervalued stocks.

We built this project to learn about sourcing and processing data ourselves for the purpose of alternative data trading, improve our abilities to work with libraries and APIs, and practice using Git and debugging projects; we succeeded at reaching that goal. The goal was not necessarily to create a safe portfolio that maximizes profit which would be useful in the real world. However, B2 was still highly successful in choosing profitable portfolios.

| ![image](https://user-images.githubusercontent.com/87958079/211218481-c3b136f9-3788-4bc7-a046-4bbe5a443c8c.png) |
|:--:| 
| *The B2 portfolios beat the S&P 500 by a huge 1212% and 817%, respectively, between Jan 1, 2008 and Dec 31, 2022.* |

## How to Install and Run
Download the project as a .zip file and extract it onto your computer. Run the main method. You will need to install pytrends, pynytimes, pandas, cohere, configparser, and yfinance using a package installer such as pip. Create your own config.ini file in the NYTScraper folder with your own free API keys for pynytimes and Cohere.

## How to Use
Run main.py in the main folder, passing in the year you want to analyze in generateTickersByYear(), and making sure all the functions are uncommented. Wait for API calls to finish, and the .json and .txt files in the TempFiles folder should update with the chosen portfolio and results. It is set to parse the last month of the year's Google Trends data, and the full year's NYT articles. You can change these timeframes yourself in the respective files, at the cost of runtime and potentially reaching the API call limits.

![image](https://user-images.githubusercontent.com/87958079/211220314-a8b43d26-99cc-4045-bac1-b80860ec39a1.png)

## Credits
This project was co-created by Ryan Shen and Alex Zhu, with research and use of:
- https://quantpedia.com/six-examples-of-trading-strategies-that-use-alternative-data/
- https://medium.com/swlh/build-an-ai-stock-trading-bot-for-free-4a46bec2a18
- https://web.archive.org/web/20160402172246/http://siblisresearch.com/data/historical-components-nasdaq 
- https://medium.com/analytics-vidhya/compare-more-than-5-keywords-in-google-trends-search-using-pytrends-3462d6b5ad62
- https://www.portfoliovisualizer.com/backtest-portfolio#analysisResults
