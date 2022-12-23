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

def exportFinalScores():
    json_list = json.dumps(config.finalScores)
    with open('TempFiles/finalScores.json', 'w', encoding='utf-8') as f:
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
    yearNumTickers = []
    with open('TempFiles/yearNumTickers.json') as json_file:
        yearNumTickersFile = json.load(json_file)
    yearNumTickers = json.loads(yearNumTickersFile)
    year = yearNumTickers[0]

    output = "Portfolio for " + str(year) + "\n"
    for x in config.portfolio:
        output += x + "\n"
    print(output)

    with open("TempFiles/Portfolio.txt", "w") as text_file:
        text_file.write(output)

def sumScore():
    localSearchScores = []
    with open('TempFiles/searchScores.json') as json_file:
        localSearchScoresFile = json.load(json_file)
    localSearchScores = json.loads(localSearchScoresFile)

    localNYTScores = []
    with open('TempFiles/NYTScores.json') as json_file:
        localNYTScoresFile = json.load(json_file)
    localNYTScores = json.loads(localNYTScoresFile)
    
    for idx, x in enumerate(localSearchScores):
        score = -1
        if (localNYTScores[idx] != -1 and x != 0):
            score = localNYTScores[idx] - x
        # else:
        #     print("stock had error, don't pick: " + str(idx))
        config.finalScores.append(score)
    
    exportFinalScores()