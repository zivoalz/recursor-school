
# path of daily returns
#prints a path of daily stock returns
# S subscript t = S subcript t-1  * Exp(-1/2 sigma^2 + sigma * sqrt(t) * W subscript t)

import random
import math

random.seed()
annualVol = .157 # annual standard deviation of returns
annualTradingDays = 248
assetPrice = 100.00 # initial asset price

# path of daily returns for year with 248 days of trading
for i in range(annualTradingDays):
    ranNorm = random.normalvariate(0,1)
    assetPrice = assetPrice * math.exp(-0.5 * math.pow(annualVol,2.0) * (1.0/annualTradingDays) + annualVol * math.pow(1.0/annualTradingDays, .5) * ranNorm)
    print assetPrice
