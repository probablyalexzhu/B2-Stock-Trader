import cohere
import configparser
from cohere.classify import Example
import pandas as pd

config = configparser.ConfigParser()
config.read('NYTScraper\config.ini')
api_key = config['cohere']['cohere_key']
co = cohere.Client(api_key)

# write some example headline analyzers

examples=[
  Example("The order came 5 days early", "positive"), 
  Example("The item exceeded my expectations", "positive"), 
  Example("I want to return my item", "negative"), 
  Example("The item's material feels low quality", "negative"), 
  Example("The order came 5 days early", "positive"), 
  Example("The item exceeded my expectations", "positive"), 
  Example("I ordered more for my friends", "positive"), 
  Example("I would buy this again", "positive"), 
  Example("I would recommend this to others", "positive"), 
  Example("The package was damaged", "negative"), 
  Example("The order is 5 days late", "negative"), 
  Example("The order was incorrect", "negative"), 
  Example("I want to return my item", "negative"), 
  Example("The item\'s material feels low quality", "negative"),
  Example("I'm so proud of you", "positive"), 
  Example("What a great time to be alive", "positive"), 
  Example("That's awesome work", "positive"), 
  Example("The service was amazing", "positive"), 
  Example("I love my family", "positive"), 
  Example("They don't care about me", "negative"), 
  Example("I hate this place", "negative"), 
  Example("The most ridiculous thing I've ever heard", "negative"), 
  Example("I am really frustrated", "negative"), 
  Example("This is so unfair", "negative"),
]

# def printScoresExample():
  # make new inputs
inputs=[
  "This item was broken when it arrived",
  "The product is amazing",
  "The product was not too bad",
]

response = co.classify(
  model='medium',
  inputs=inputs,
  examples=examples,
)
print(response.classifications)
print("now magic ")
positive_confidences = []

for classification in response.classifications:
  print(response.classifications.labels)


print(pos-neg)

#return positive - negative 
# loop through these to put these into config.NYTScores

def getInputs(idx):
  df = pd.read_excel(open('ArticleHeadlines.xlsx', 'rb'), sheet_name=str(idx))
  articles = df["headline"]
  list = []
  for x in articles:
    list.append(x)
  print(list)