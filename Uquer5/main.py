import MFMC as MC
import pandas as pd
from matplotlib import pylab

import seaborn as sns
startdate = '2013-04-11'
enddate = '2013-08-09'
TGT = MC.MarketUniverse()
TGT.initializeFromTickers('TGT')
#print(AAPL.MKTUNIV)
TGTStrategy = MC.MACDStrategy(TGT,startdate,enddate)
trade = TGTStrategy.tradeRetrun()

# print(trade)
pylab.figure(figsize=(12,8))
pylab.subplot(211)
pylab.plot(TGT.MKTUNIV.loc[startdate:enddate]['close'])
pylab.subplot(212)
pylab.plot(TGTStrategy .signal[['MACD','signalLine']])
pylab.show()
pylab.figure(figsize=(12,8))
pylab.plot(trade[['CMarket','CStrategy']])
pylab.legend(('Market','Strategy'),loc = 'upper right')
pylab.show()


#print(marketFactor.tickerToMarketFactorDict['NKE'])

