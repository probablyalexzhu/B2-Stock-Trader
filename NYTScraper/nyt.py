# import necessary packages (I installed via command line with: python -m pip install --upgrade pynytimes)
# pynytimes documentation: https://github.com/michadenheijer/pynytimes#archive-metadata
from pynytimes import NYTAPI
import datetime
import pandas as pd
import configparser

# initiate connection w/ personal API key
config = configparser.ConfigParser()
config.read('Twitter Scraper\config.ini')

api_key = config['NYT']['NYT_key']
nyt = NYTAPI(api_key, parse_dates=True)

articles = nyt.article_search(
    query = "Tesla",
    results = 1,
    dates = {
        "begin": datetime.datetime(2015, 1, 1),
        "end": datetime.datetime(2016, 1, 1)
    }
)
#Assign the data in the first item of articles to a variable
article = articles[0].copy()

#useful data: abstract, snippet, lead_paragraph, print_headline
#Recommended deleting the multimedia key to reduce clutter in the data

print(article)

# for each of the articles in the list, get the information that is stored in a nested dictionary:
headline = map(lambda x: x["headline"]["main"], articles)
# author = map(lambda x: x["headline"]["kicker"], articles)
# leadparagraph = map(lambda x: x["lead_paragraph"], articles)
# pubdate = map(lambda x: x["pub_date"], articles)
body = map(lambda x: x["body"], articles)

# since keywords are a branch down in the nested dictionary, we need to add an additional for loop to collect all keywords:
#keywords = map(lambda x:list(i["value"] for i in x["keywords"]), articles)

# transforming the data into a pandas dataframe:
#data={'headline': list(headline), 'author': list(author), 'leadparagraph':list(leadparagraph),'publication date': list(pubdate), "keywords": list(keywords)}
data={'headline': list(headline), 'body': list(body)}
df = pd.DataFrame(data)

# exporting the data to csv:
df.to_csv('NYT_data.csv')



print('done')
nyt.close()