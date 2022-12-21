# Author: Alex Zhu
# Last Updated: Dec 20, 2022
# Help from https://medium.com/analytics-vidhya/compare-more-than-5-keywords-in-google-trends-search-using-pytrends-3462d6b5ad62

import pandas as pd                        
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import numpy as np
import tickerparser

list1=['AAL','AAPL','ADBE', 'ADP','ADI']
list2=['ADI', 'ADSK' ,'AKAM','AMAT' ,'AMGN']

pytrends1=TrendReq()
pytrends2=TrendReq()

pytrends1.build_payload(list1,geo='US',timeframe="2016-12-14 2017-01-25")
pytrends2.build_payload(list2,geo='US',timeframe="today 12-m")

df1=pytrends1.interest_over_time()
df2=pytrends2.interest_over_time()

averageList1=[]
averageList2=[]
for item in list1:
    averageList1.append(df1[item].mean().round(0))
for item in list2:
    averageList2.append(df2[item].mean().round(0))

normalizationFactor=averageList1[0]/averageList2[0]

for i in range(len(averageList2)):
    normalisedVal=normalizationFactor*averageList2[i]
    averageList2[i]=normalisedVal.round(0)
averageList2.pop(0)
list2.pop(0)

TVSeriesList=list1+list2

finalAverageList=averageList1+averageList2

y_pos=np.arange(len(TVSeriesList))
plt.barh(y_pos,finalAverageList,align='center',alpha=0.5)
plt.yticks(y_pos,TVSeriesList)
plt.xlabel('Average popularity')
plt.show()