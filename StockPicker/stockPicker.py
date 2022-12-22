import config

def pickStocks():
    for idx, x in enumerate(config.sumScores):
        if x > 1.5:
            config.portfolio.append(config.namesFiltered[idx] + ", " + str(x))