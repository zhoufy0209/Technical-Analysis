import numpy as np
import pandas as pd
import math
import os
import collections



class MarketUniverse:
    def __init__(self):
       self.MKTUNIV =pd.DataFrame()

    def initializeFromFileName(self,dataFileName):
        columnNames = ['date','time','open','high','low','close','volume']
        ticker = dataFileName[6:dataFileName.find('.')].upper() #print ticker
        self.MKTUNIV = pd.read_csv('F:/Local-Repository/daily/'+dataFileName)
        self.MKTUNIV.columns = columnNames
        self.MKTUNIV['date'] = self.MKTUNIV['date'].apply(lambda x : pd.to_datetime(x,format='%Y%m%d'))
        for columnName in columnNames:
            if columnName == 'time':
                self.MKTUNIV.drop('time',axis=1,inplace= True)
        self.MKTUNIV['return'] = np.log(self.MKTUNIV['close']/self.MKTUNIV['close'].shift(1))
        self.MKTUNIV = self.MKTUNIV.set_index(['date'])

    def initializeFromTickers(self,ticker):
        if type(ticker)!= str:
            print('Ticker should be a str.')
        else:
            self.initializeFromFileName('table_'+ ticker.lower() + '.csv')

    def SMA(self,item,stardate,enddate,n):
        return np.round(self.MKTUNIV.loc[stardate:enddate][item].rolling(window = n, center = False).mean(),5)

    def EMA(self,item,stardate,enddate,n):
         return np.round(self.MKTUNIV.loc[stardate:enddate][item].ewm(span=n,min_periods=0,adjust=True,ignore_na=False).mean(), 5)





class Strategy:
    def __init__(self,ticker,startdate,enddate,init_capital = 10000):
        self.ticker = ticker
        self.startdate = startdate
        self.enddate = enddate
        self.init_capital = init_capital

    def tradeRetrun(self):
        startdate = self.signal.index[0]
        enddate = self.signal.index[-1]
        tradeReturn = pd.DataFrame(index =self.signal.index)
        tradeReturn['Market'] = self.ticker.MKTUNIV['return'].loc[startdate:enddate]
        tradeReturn['Strategy'] = self.ticker.MKTUNIV['return'].loc[startdate:enddate] * self.signal['action'].shift(1)
        tradeReturn[['CMarket','CStrategy']] = tradeReturn[['Market','Strategy']].cumsum()
        tradeReturn[['Market Cash','Strategy Cash']] =tradeReturn[['CMarket','CStrategy']].apply(np.exp)*self.init_capital
        return tradeReturn








class MACDStrategy(Strategy):
    def __init__(self,ticker,startdate,enddate):
        Strategy.__init__(self,ticker,startdate,enddate,init_capital = 10000 )
        self.signal = self.gen_signal()

    def gen_signal(self):
        signal = pd.DataFrame(index=self.ticker.MKTUNIV.loc[self.startdate:self.enddate].index)
        signal['MACD'] = self.ticker.EMA('close',self.startdate,self.enddate,12)-self.ticker.EMA('close',self.startdate,self.enddate,26)
        signal['signalLine'] = np.round(signal['MACD'].ewm(span=9,min_periods=0,adjust=True,ignore_na=False).mean(),5)
        signal['M-Signal'] = signal['MACD']-signal['signalLine']
        signal['action'] = np.where(signal['M-Signal']>0,1,0)
        return signal







class MAStrategy(Strategy):
    def __init__(self,ticker,startdate,enddate,short_window,long_window,SD):
        Strategy.__init__(self,ticker,startdate,enddate,init_capital = 10000)
        self.short_window = short_window
        self.long_window = long_window
        self.SD = SD
        self.signal = self.gen_signal()


    def gen_signal(self):
        signal = pd.DataFrame(index = self.ticker.MKTUNIV.loc[self.startdate:self.enddate].index)
        short_MA = self.ticker.SMA('close',self.startdate,self.enddate,self.short_window)
        long_MA = self.ticker.SMA('close',self.startdate,self.enddate,self.long_window)
        signal['s-l'] = short_MA - long_MA
        signal['action'] = np.where(signal['s-l']>self.SD,1,0)
        return signal





