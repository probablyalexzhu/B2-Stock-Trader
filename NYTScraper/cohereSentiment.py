import json
import cohere
import configparser
from StockPicker.configexporter import exportNYTScores
import config
from cohere.classify import Example
import pandas as pd

config2 = configparser.ConfigParser()
config2.read('NYTScraper\config.ini')
api_key = config2['cohere']['cohere_key']
co = cohere.Client(api_key)

examples=[
  Example("Apple’s Cut From App Sales Reached $4.5 Billion in 2014", "positive"),
  Example("Tests of Cholesterol Drugs Offer Hope of Reducing Heart Attacks and Strokes", "positive"),
  Example("F.D.A. Approves Amgen Drug to Treat Heart Failure", "positive"),
  Example("With Win, Amazon Shakes Up Yet Another Industry", "positive"),
  Example("Bobby Kotick’s Activision Blizzard to Buy King Digital, Maker of Candy Crush", "positive"),
  Example("Biogen Reports Its Alzheimer’s Drug Sharply Slowed Cognitive Decline", "positive"),
  Example("Intel Agrees to Buy Altera for $16.7 Billion", "positive"),
  Example("SodaStream Hits Reset as Its Sales and Profit Fall", "negative"),
  Example("Amazon’s Tax Deal With Luxembourg May Break Rules, E.U. Regulator Says", "negative"),
  Example("Comcast-Time Warner Cable Deal’s Collapse Leaves Frustrated Customers Out in the Cold", "negative"),
  Example("Daily Report: Tech Giants Said to Offer Bigger Settlement in Antitrust Case on Hiring", "negative"),
  Example("C.F.T.C. Accuses Kraft and Mondelez of Manipulating Wheat Prices", "negative"),
  Example("Morning Agenda: Split Decision for Greenberg in A.I.G. Lawsuit", "negative"),
  Example("Apple’s New Job: Selling a Smartwatch to an Uninterested Public", "negative")
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
  localHeadLineLists = []
  with open('TempFiles/headlineLists.json') as json_file:
    localHeadLineListsFile = json.load(json_file)
  localHeadLineLists = json.loads(localHeadLineListsFile)

  return localHeadLineLists[idx]

def generateNYTScores():
  for i in range(0, 1):
    cohereSentiment(examples, i)
  exportNYTScores()