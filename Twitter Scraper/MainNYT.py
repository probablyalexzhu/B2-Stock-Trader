
import pandas as pd

df = pd.read_excel(open('GoogleScraper/Tickers.xlsx', 'rb'), sheet_name='NYSE')
namesUnfiltered = df["Company"]