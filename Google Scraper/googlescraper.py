import pandas as pd                        
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

kw_list=['Soccer', 'Football', 'Disney', 'Andor', 'Waterloo']
pytrends.build_payload(kw_list, timeframe='today 1-m')

# Interest by Region
regiondf = pytrends.interest_by_region()
#looking at rows where all values are not equal to 0
regiondf = regiondf[(regiondf != 0).all(1)]

#drop all rows that have null values in all columns
regiondf.dropna(how='all',axis=0, inplace=True)

#visualise
regiondf.plot(figsize=(20, 12), y=kw_list, kind ='bar')

regiondf.to_excel("pytrends2.xlsx", sheet_name="FTX", index=False)