# import necessary packages (I installed via command line with: python -m pip install --upgrade pynytimes)
# pynytimes documentation: https://github.com/michadenheijer/pynytimes#archive-metadata
from pynytimes import NYTAPI
import datetime
import pandas as pd
import configparser
import config
import os
from openpyxl import load_workbook
import json
from StockPicker.configexporter import *

# initiate connection w/ personal API key
configp = configparser.ConfigParser()
configp.read('NYTScraper\config.ini')

api_key = configp['NYT']['NYT_key']
nyt = NYTAPI(api_key, parse_dates=True)

def generateArticleText():
    
    localNamesFiltered = []
    with open('TempFiles/namesFiltered.json') as json_file:
        localNamesFilteredFile = json.load(json_file)
    localNamesFiltered = json.loads(localNamesFilteredFile)

    yearNumTickers = []
    with open('TempFiles/yearNumTickers.json') as json_file:
        yearNumTickersFile = json.load(json_file)
    yearNumTickers = json.loads(yearNumTickersFile)
    year = yearNumTickers[0]
    numTickers = yearNumTickers[1]

    for i in range(0, numTickers): # be very patient
        config.headlineLists.append(getArticles(localNamesFiltered[i], year).values.tolist())
        # with open("ArticleHeadlines.txt", "w") as text_file:
        #     text_file.write(str(headlineList))

        print("done" + str(i))
    nyt.close()

    # print(config.headlineLists)
    exportHeadlineLists()

def getArticles(q, year):
    articles = nyt.article_search(
        query = q,
        # results = 1,
        dates = {
            "begin": datetime.datetime(year - 1, 1, 1),
            "end": datetime.datetime(year, 1, 1)
        },
        options = {
        "sort": "oldest",
        "sources": [
            "New York Times",
            "AP",
            "Reuters",
            "International Herald Tribune"
        ]
        }
    )

    # for each of the articles in the list, get the information that is stored in a nested dictionary:
    headline = map(lambda x: x["headline"]["main"], articles)
    # leadparagraph = map(lambda x: x["lead_paragraph"], articles)
    # maybe add abstract in final version

    # transforming the data into a pandas dataframe:
    #data={'headline': list(headline), 'author': list(author), 'leadparagraph':list(leadparagraph),'publication date': list(pubdate), "keywords": list(keywords)}
    data={'headline': list(headline)}
    df = pd.DataFrame(data)
    return df