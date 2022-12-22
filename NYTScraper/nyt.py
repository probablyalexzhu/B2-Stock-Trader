# import necessary packages (I installed via command line with: python -m pip install --upgrade pynytimes)
# pynytimes documentation: https://github.com/michadenheijer/pynytimes#archive-metadata
from pynytimes import NYTAPI
import datetime
import pandas as pd
import configparser
import config
# initiate connection w/ personal API key
configp = configparser.ConfigParser()
configp.read('NYTScraper\config.ini')

api_key = configp['NYT']['NYT_key']
nyt = NYTAPI(api_key, parse_dates=True)

def getArticles(q):
    articles = nyt.article_search(
        query = q,
        results = 1,
        dates = {
            "begin": datetime.datetime(config.yearToAnalyze - 1, 1, 1),
            "end": datetime.datetime(config.yearToAnalyze, 1, 1)
        }
    )

    # for each of the articles in the list, get the information that is stored in a nested dictionary:
    headline = map(lambda x: x["headline"]["main"], articles)
    leadparagraph = map(lambda x: x["lead_paragraph"], articles)
    # maybe add abstract in final version

    # transforming the data into a pandas dataframe:
    #data={'headline': list(headline), 'author': list(author), 'leadparagraph':list(leadparagraph),'publication date': list(pubdate), "keywords": list(keywords)}
    data={'headline': list(headline), 'leadparagraph':list(leadparagraph)}
    df = pd.DataFrame(data)
    nyt.close()
    return df