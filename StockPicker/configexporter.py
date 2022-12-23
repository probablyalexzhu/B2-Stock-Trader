import config
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json

# def exportConfig():
#     columns=['Tickers','Names', 'Search', 'Sentiment', 'Sum']
#     df = pd.DataFrame(list(zip(config.tickersFiltered,config.namesFiltered, config.googAverageListFinal), config.NYTScores, config.sumScores), columns=columns)
#     df.to_excel('ConfigSheet.xlsx')

def exportTickersFiltered():
    json_list = json.dumps(config.tickersFiltered)
    with open('TempFiles/tickersFiltered.json', 'w', encoding='utf-8') as f:
        json.dump(json_list, f, ensure_ascii=False, indent=4)

def exportNamesFiltered():
    json_list = json.dumps(config.namesFiltered)
    with open('TempFiles/namesFiltered.json', 'w', encoding='utf-8') as f:
        json.dump(json_list, f, ensure_ascii=False, indent=4)

def exportYearNumTickers():
    yearNumTickers = []
    yearNumTickers.append(config.yearToAnalyze)
    yearNumTickers.append(config.numTickers)
    json_list = json.dumps(yearNumTickers)
    with open('TempFiles/yearNumTickers.json', 'w', encoding='utf-8') as f:
        json.dump(json_list, f, ensure_ascii=False, indent=4)

def exportSearchScores():
    json_list = json.dumps(config.searchScores)
    with open('TempFiles/searchScores.json', 'w', encoding='utf-8') as f:
        json.dump(json_list, f, ensure_ascii=False, indent=4)

def exportHeadlineLists():
    json_list = json.dumps(config.headlineLists)
    with open('TempFiles/headlineLists.json', 'w', encoding='utf-8') as f:
        json.dump(json_list, f, ensure_ascii=False, indent=4)

def exportNYTScores():
    json_list = json.dumps(config.NYTScores)
    with open('TempFiles/NYTScores.json', 'w', encoding='utf-8') as f:
        json.dump(json_list, f, ensure_ascii=False, indent=4)

def graph():

    localTickersFiltered = []
    with open('TempFiles/tickersFiltered.json') as json_file:
        localTickersFilteredFile = json.load(json_file)
    localTickersFiltered = json.loads(localTickersFilteredFile)

    localSearchScores = []
    with open('TempFiles/searchScores.json') as json_file:
        localSearchScoresFile = json.load(json_file)
    localSearchScores = json.loads(localSearchScoresFile)

    print(localTickersFiltered)
    print(localSearchScores)

    y_pos=np.arange(len(localTickersFiltered))
    plt.barh(y_pos,localSearchScores,align='center',alpha=0.5)
    plt.yticks(y_pos,localTickersFiltered)
    plt.xlabel('Search Volume')
    plt.show()

def printPortfolio():
    print("### PORTFOLIO OF SHIT TO BUY AT YOUR OWN RISK ###")
    print(config.portfolio)

    with open("Portfolio.txt", "w") as text_file:
        text_file.write(str(config.portfolio))

def sumScore():
    # sus temporary code
    df = pd.read_excel(open('ConfigSheet.xlsx', 'rb'), sheet_name='Sheet1')
    config.NYTScores = df["Sentiment"]
    for idx, x in enumerate(config.searchScores):
        config.finalScores.append(config.NYTScores[idx] - x)