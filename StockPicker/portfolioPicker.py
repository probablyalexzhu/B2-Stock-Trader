import config

def pickStocks():
    for idx, x in enumerate(config.sumScores):
        if x > 0.75:
            config.portfolio.append(config.tickersFiltered[idx] + ": " + config.namesFiltered[idx] + ", " + str(x))