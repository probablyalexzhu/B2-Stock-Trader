import cohere
import configparser
from cohere.classify import Example

def printScoresExample():
  config = configparser.ConfigParser()
  config.read('Twitter Scraper\config.ini')
  api_key = config['cohere']['cohere_key']
  co = cohere.Client('gm8A89mCG1RJmWhk8whhPlpete9K3Z61WKlTDwIi')

  # write some example headline analyzers

  examples=[
    Example("The order came 5 days early", "positive"), 
    Example("The item exceeded my expectations", "positive"), 
    Example("I want to return my item", "negative"), 
    Example("The item\'s material feels low quality", "negative"), 
  ]

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
  print("hello!")
  print(response.classifications)

  # loop through these to put these into config.NYTScores