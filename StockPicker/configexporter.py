import config
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def exportConfig():
    columns=['Tickers','Names', 'Search', 'Sentiment', 'Sum']
    df = pd.DataFrame(list(zip(config.tickersFiltered,config.namesFiltered, config.googAverageListFinal), config.NYTScores, config.sumScores), columns=columns)
    df.to_excel('ConfigSheet.xlsx')

def graph():
    y_pos=np.arange(len(config.tickersFiltered))
    plt.barh(y_pos,config.googAverageListFinal,align='center',alpha=0.5)
    plt.yticks(y_pos,config.tickersFiltered)
    plt.xlabel('Search volume')
    plt.show()

def printPortfolio():
    print("### PORTFOLIO OF SHIT TO BUY AT YOUR OWN RISK ###")
    print(config.portfolio)

    text_file = open("portfolio.txt", "w")
    n = text_file.write(str(config.portfolio))
    text_file.close()


def sumScore():
    for idx, x in enumerate(config.googAverageListFinal):
        config.sumScores.append((config.googAverageListFinal[idx] + config.NYTScores[idx]) / 2)