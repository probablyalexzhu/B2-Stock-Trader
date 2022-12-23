import datetime
import backtrader as bt

class SmaCross(bt.SignalStrategy):
    def __init__(self):
        pass
        sma = bt.ind.SMA(period=50)
        price = self.data
        crossover = bt.ind.CrossOver(price, sma)
        self.signal_add(bt.SIGNAL_LONG, crossover)

overallProfit = 0

# settings for out-of-sample data
# fromdate=datetime.datetime(2018, 1, 1),
# todate=datetime.datetime(2019, 12, 25))
tickers = {"BIIB": 0.63,
            "KLAC": 0.58,
            "GILD": 0.54,
            "AMGN": 0.47,
            "TXN": 0.45,
            "ATVI": 0.32,
            "JD": 0.28,
            "NXPI": 0.23,
            "REGN": 0.22,
            "EBAY":0.21}

for ticker, target in tickers.items():
    cerebro = bt.Cerebro()
    data = bt.feeds.YahooFinanceData(
        dataname="Backtester/" + ticker + ".csv",
        timeframe=bt.TimeFrame.Days,
        fromdate=datetime.datetime(2017, 1, 1),
        todate=datetime.datetime(2022, 1, 1),
        reverse=False,
    )
    data.target = target
    cerebro.adddata(data, name=ticker)
    print("done")

    cerebro.addsizer(bt.sizers.AllInSizer, percents=95)
    # Add strategy to Cerebro
    # cerebro.addstrategy()

    cerebro.addstrategy(SmaCross)

    start_portfolio_value = cerebro.broker.getvalue()

    cerebro.run()
    # cerebro.plot()

    end_portfolio_value = cerebro.broker.getvalue()
    pnl = end_portfolio_value - start_portfolio_value
    print(f'Starting: {start_portfolio_value:2f}')
    print(f'Final: {end_portfolio_value:2f}')
    print(f'PnL: {pnl:.2f}')
    overallProfit += pnl

print("Starting Portfolio Value: " + str(100000))
print(f'Final Portfolio PnL: {100000+overallProfit:2f}')
print(f'PnL: {overallProfit:2f}')