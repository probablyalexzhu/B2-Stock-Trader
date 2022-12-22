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

def createPortfolio():
    print("### PORTFOLIO OF SHIT TO BUY AT YOUR OWN RISK ###")
    print(config.portfolio)

    with open("Portfolio.txt", "w") as text_file:
        text_file.write(str(config.portfolio))


def sumScore():
    for idx, x in enumerate(config.googAverageListFinal):
        config.sumScores.append((config.googAverageListFinal[idx] + config.NYTScores[idx]) / 2)