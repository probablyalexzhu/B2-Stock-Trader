import config

def pickStocks():
    for idx, x in enumerate(config.finalScores):
        if x > 0.5:
            config.portfolio.append(config.tickersFiltered[idx] + ": " + config.namesFiltered[idx] + ", " + str(x))