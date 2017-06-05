# path of daily returns
#prints a path of daily stock returns
# Nassim Taleb's - dynanic hedging exercise
# S subscript t = S subcript t-1  * Exp(-1/2 sigma^2 + sigma * sqrt(t) * W subscript t)

import random
import math
# import numpy #not used
import pylab # graphing library

random.seed()
annualVol = .157 # annual standard deviation of returns
annualTradingDays = 248
assetPrice = 100.00 # initial asset price

prices =[]
days = []
prices.append(assetPrice)
days.append(0) # starting time

# path of daily returns for year with 248 days of trading
for i in range(1 , annualTradingDays + 1): # range goes to -1 of max
    ranNorm = random.normalvariate(0,1)
    days.append(i)
    assetPrice = assetPrice * math.exp(-0.5 * math.pow(annualVol,2.0) * (1.0/annualTradingDays) + annualVol * math.pow(1.0/annualTradingDays, .5) * ranNorm)
    prices.append(assetPrice)
else:
    # print prices # for testing
    # print days   # for testing

# use pylab to plot data both the x and y
    pylab.plot(days, prices)

# axis lables
    pylab.xlabel('Trading Days')
    pylab.ylabel('Asset Price')

# title
    pylab.title('Geometric Brownian Motion')

# show the graphing
    pylab.show()

