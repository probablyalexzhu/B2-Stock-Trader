import config
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def exportConfig():
    columns=['Tickers','Names', 'Search']
    df = pd.DataFrame(list(zip(config.tickersFiltered,config.namesFiltered, config.averageListFinal)), columns=columns)
    df.to_excel('ConfigSheet.xlsx')

def graph():
    # GrAPH it
    y_pos=np.arange(len(config.tickersFiltered))
    plt.barh(y_pos,config.averageListFinal,align='center',alpha=0.5)
    plt.yticks(y_pos,config.tickersFiltered)
    plt.xlabel('Average search density')
    plt.show()