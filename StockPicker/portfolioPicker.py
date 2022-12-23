import config
import json

def pickStocks():
    localFinalScores = []
    with open('TempFiles/finalScores.json') as json_file:
        localFinalScoresFile = json.load(json_file)
    localFinalScores = json.loads(localFinalScoresFile)

    localTickersFiltered = []
    with open('TempFiles/tickersFiltered.json') as json_file:
        localTickersFilteredFile = json.load(json_file)
    localTickersFiltered = json.loads(localTickersFilteredFile)

    localNamesFiltered = []
    with open('TempFiles/namesFiltered.json') as json_file:
        localNamesFilteredFile = json.load(json_file)
    localNamesFiltered = json.loads(localNamesFilteredFile)

    indexesOfBestStocks = []

    i = 0
    while (i < 10 and max(localFinalScores) > 0):
        indexesOfBestStocks.append(localFinalScores.index(max(localFinalScores)))
        localFinalScores[localFinalScores.index(max(localFinalScores))] = -1
        i += 1
    
    localFinalScores = json.loads(localFinalScoresFile) # to get values back so they aren't -1
    # print("indexes: " + str(indexesOfBestStocks))

    for idx, x in enumerate(indexesOfBestStocks):
        config.portfolio.append(localTickersFiltered[x] + ": " + localNamesFiltered[x] + ", " + str("{:.2f}".format(localFinalScores[x])))