import cohere
import configparser
import config
from cohere.classify import Example
import pandas as pd

config2 = configparser.ConfigParser()
config2.read('NYTScraper\config.ini')
api_key = config2['cohere']['cohere_key']
co = cohere.Client(api_key)

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

def cohereSentiment(examples, idx):
  inputs2 = getInputs(idx)
  if len(inputs2)==0:
    pos = -1
  else:
    response = co.classify(
      model='medium',
      inputs=inputs2,
      examples=examples,
    )
    positive_confidences = []

    for classification in response.classifications:
      if classification.prediction == "positive":
        positive_confidences.append(classification.confidence)
      elif classification.prediction == "negative":
        positive_confidences.append(1-classification.confidence)

    pos = sum(positive_confidences)
    pos /=len(inputs2)
  pos = round(pos, 3)
  print(pos)
  config.NYTScores.append(pos)

  #return positive - negative 
  # loop through these to put these into config.NYTScores

def getInputs(idx):
  df = pd.read_excel(open('ArticleHeadlines.xlsx', 'rb'), sheet_name=str(idx))
  articles = df["headline"]
  list = []
  for x in articles:
    list.append(x)
  return list

def generateNYTScores():
  for i in range(0, 82): # set this to length of tickersFiltered
    cohereSentiment(examples, i)