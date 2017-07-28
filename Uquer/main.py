<<<<<<< HEAD
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
#create series
# a = np.random.randn(5)
# print("a is an array:")
# print(a)
# s = Series (a)
# print("s is a series:")
# print(s)

# s1 = Series(np.random.rand(5), index = ['a','b','c','d','e'],name = 'my_series')
# print(s1)
# print(s1.name)

#create series from a dict
# d = {'A': 1., 'B': 2., "C": 3.}
# print('d is a dict:')
# print(d)
# s = Series(d)
# print('s is a Seires:')
# print(s)
# print(Series(d,index=['A', 'C', 'B','D'],name = 'my_series'))

#create DataFrame from a dict with value of  list
#lists should be of same length
# d = {'one': [1., 2., 3., 4.], 'two': [4., 3., 2., 1.]}
# df = DataFrame(d,index = ['a', 'b', 'c', 'e'])
# print(df)

# d= [{'a': 1.6, 'b': 2}, {'a': 3, 'b': 6, 'c': 9}]
# df = DataFrame(d)
# print(df)

#concat combines Series. axis = 1 column axis = 0 row
# a = Series(range(5))
# b = Series(np.linspace(4,20,5))
# df = pd.concat([a,b],axis = 0)
# print(df)


#glue several DataFrame together, create a larger DataFrame
#axis = 0
# df = DataFrame()
# index = ['alpha', 'beta', 'gamma', 'delta', 'eta']
# for i in range(5):
#     a = DataFrame([np.linspace(i,5*i,5)],index = [index[i]])
#     df = pd.concat([df,a],axis = 0)
#print(df)

#axis = 1
#用列表生成dataframe只能按行生成，但是可以通过dict按列生成
# df = { }
# index =['alpha', 'beta', 'gamma', 'delta', 'eta']
# for i in range(5):
#     a = Series(np.linspace(0,4*(i+1),5,True),index = index)
#     df[i] = a
# print(DataFrame(df))

#DataFrame访问

#print(df[1])
#print(type(df[1]))
#df.columns = ['a','b','c','d','e']
#print(df)
#print( df[['c', 'd']])
# print(type(df[['c', 'd']]))
#print (df['b'][2])
#df.iloc 按下标取
#print (df.iloc[1])
#df.loc 按索引取
#print(df.loc['alpha'])

# Selecting by slicing
#print(df[1:3])

#a series with elements date
# dates = pd.date_range('20170701',periods=5)
# df = DataFrame(np.random.randn(5,4),index = dates,columns=['a','b','c','d'])
# print(df)

df =DataFrame()
df = pd.read_csv('daily/A.csv')
df.columns=['Date','Open','High','Low','Close','Adj_close','Volume']
df['Date'] = df['Date'].apply(lambda x : pd.to_datetime(x,infer_datetime_format=True))
#print("Order by column values, descending:")
#print(df.sort_values(by = ['High','Low'], ascending =[False,False]).head(30))
#print(df[df.Close>df.Close.mean()].sort_values(by =['Close'], ascending = [False]).head(30))
#count the frequency
#print(df.Close.value_counts().head(5))

#merge
# data1 = df[['Date','Close']]
# data2 = df[['Date','Adj_close']]
# dat = data1.merge(data2, on = ['Date'])
# print(dat.head())

#goupby

#plot
dat = df.set_index('Date')['Close']
dat.plot(title='close price of A')
=======
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
#create series
# a = np.random.randn(5)
# print("a is an array:")
# print(a)
# s = Series (a)
# print("s is a series:")
# print(s)

# s1 = Series(np.random.rand(5), index = ['a','b','c','d','e'],name = 'my_series')
# print(s1)
# print(s1.name)

#create series from a dict
# d = {'A': 1., 'B': 2., "C": 3.}
# print('d is a dict:')
# print(d)
# s = Series(d)
# print('s is a Seires:')
# print(s)
# print(Series(d,index=['A', 'C', 'B','D'],name = 'my_series'))

#create DataFrame from a dict with value of  list
#lists should be of same length
# d = {'one': [1., 2., 3., 4.], 'two': [4., 3., 2., 1.]}
# df = DataFrame(d,index = ['a', 'b', 'c', 'e'])
# print(df)

# d= [{'a': 1.6, 'b': 2}, {'a': 3, 'b': 6, 'c': 9}]
# df = DataFrame(d)
# print(df)

#concat combines Series. axis = 1 column axis = 0 row
# a = Series(range(5))
# b = Series(np.linspace(4,20,5))
# df = pd.concat([a,b],axis = 0)
# print(df)


#glue several DataFrame together, create a larger DataFrame
#axis = 0
# df = DataFrame()
# index = ['alpha', 'beta', 'gamma', 'delta', 'eta']
# for i in range(5):
#     a = DataFrame([np.linspace(i,5*i,5)],index = [index[i]])
#     df = pd.concat([df,a],axis = 0)
#print(df)

#axis = 1
#用列表生成dataframe只能按行生成，但是可以通过dict按列生成
# df = { }
# index =['alpha', 'beta', 'gamma', 'delta', 'eta']
# for i in range(5):
#     a = Series(np.linspace(0,4*(i+1),5,True),index = index)
#     df[i] = a
# print(DataFrame(df))

#DataFrame访问

#print(df[1])
#print(type(df[1]))
#df.columns = ['a','b','c','d','e']
#print(df)
#print( df[['c', 'd']])
# print(type(df[['c', 'd']]))
#print (df['b'][2])
#df.iloc 按下标取
#print (df.iloc[1])
#df.loc 按索引取
#print(df.loc['alpha'])

# Selecting by slicing
#print(df[1:3])

#a series with elements date
# dates = pd.date_range('20170701',periods=5)
# df = DataFrame(np.random.randn(5,4),index = dates,columns=['a','b','c','d'])
# print(df)

df =DataFrame()
df = pd.read_csv('daily/A.csv')
df.columns=['Date','Open','High','Low','Close','Adj_close','Volume']
df['Date'] = df['Date'].apply(lambda x : pd.to_datetime(x,infer_datetime_format=True))
#print("Order by column values, descending:")
#print(df.sort_values(by = ['High','Low'], ascending =[False,False]).head(30))
#print(df[df.Close>df.Close.mean()].sort_values(by =['Close'], ascending = [False]).head(30))
#count the frequency
#print(df.Close.value_counts().head(5))

#merge
# data1 = df[['Date','Close']]
# data2 = df[['Date','Adj_close']]
# dat = data1.merge(data2, on = ['Date'])
# print(dat.head())

#goupby

#plot
dat = df.set_index('Date')['Close']
dat.plot(title='close price of A')
>>>>>>> origin/master
plt.show()