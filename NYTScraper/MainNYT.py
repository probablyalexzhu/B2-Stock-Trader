import pandas as pd
from nyt import *
import config
namesFiltered = ["tesla", "apple"]

articleText = []

def generateArticleText():
# df = pd.read_excel(open('GoogleScraper/Tickers.xlsx', 'rb'), sheet_name='NYSE')
# namesFiltered = df["Company"].tolist()

    for company in namesFiltered:
        dataframe = getArticles(company)
        print(dataframe)