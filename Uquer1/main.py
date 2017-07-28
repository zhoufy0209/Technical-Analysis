<<<<<<< HEAD
from scipy.stats import norm
from math import log, sqrt, exp
import time
import numpy as np
from matplotlib import pylab
import seaborn as sns



spot = 2.45
maturity = 0.25
vol = 0.25
r = 0.05

def call_option_pricer(spot,strike,maturity,r,vol):
    d1 = (log(spot/strike) + (r + 0.5 * vol * vol) * maturity)/vol/sqrt(maturity)
    d2 = d1 - vol * sqrt(maturity)
    price = spot * norm.cdf(d1)-strike * exp(-r * maturity) * norm.cdf(d2)
    return price
# print(call_option_pricer(2.45,2.5,0.25,0.05,0.25))

#use numpy to accelerate
portfolioSize = range(1,10000,500)
timeSpent = []

# #before
for size in portfolioSize:
    now = time.time()
    strikes = np.linspace(2.0,3.0,size)
    for i in range(size):
        res = call_option_pricer(spot, strikes[i], maturity, r, vol)
    timeSpent.append(time.time() - now)


# sns.set(style="ticks")
# pylab.figure(figsize = (12,8))
# pylab.bar(portfolioSize, timeSpent, color = 'r', width =300)
# pylab.grid(True)
# pylab.title('time of calculation (s)',fontsize = 18)
# pylab.ylabel('time（s)', fontsize = 15)
# pylab.xlabel('numbers', fontsize = 15)
# pylab.show()
#
# #all functions in Numpy can apply to a list of number, i.e vectors.
def call_option_pricer_numpy(spot, strike, maturity, r, vol):
    d1 = (np.log(spot/strike) + (r + 0.5 * vol * vol)*maturity)/vol/np.sqrt(maturity)
    d2 = d1 - vol * np.sqrt(maturity)
    price = spot * norm.cdf(d1) - strike * np.exp(-r * maturity) * norm.cdf(d2)
    return price


timeSpentNumpy = []
for size in portfolioSize:
    now = time.time()
    strikes = np.linspace(2.0, 3.0, size)
    res = call_option_pricer_numpy(spot, strikes, maturity, r, vol)
    timeSpentNumpy.append(time.time() - now)

sns.set(style="ticks")
# pylab.figure(figsize = (12,8))
# pylab.bar(portfolioSize, timeSpentNumpy, color = 'r', width =300)
# pylab.grid(True)
# pylab.title('time of calculation_numpy (s)',fontsize = 18)
# pylab.ylabel('time（s)', fontsize = 15)
# pylab.xlabel('numbers', fontsize = 15)
# #pylab.show()

fig = pylab.figure(figsize=(12,8))
ax = fig.gca()
pylab.plot(portfolioSize,np.log10(timeSpent),portfolioSize, np.log10(timeSpentNumpy))  #make multiple line with one commmand
pylab.grid(True) #grid 网格
from matplotlib.ticker import FuncFormatter
# def millions(x, pos):
#     'The two args are the value and tick position'
#     return '$10^{%.0f}$' % (x)
# formatter = FuncFormatter(millions)
# ax.yaxis.set_major_formatter(formatter)
pylab.title('time(s)', fontsize = 18)
pylab.legend(['iterating', 'numpy_version'], loc = 'upper center', ncol = 2)
pylab.ylabel('log10 of time(s)', fontsize = 15)
pylab.xlabel('number',  fontsize = 15)
=======
from scipy.stats import norm
from math import log, sqrt, exp
import time
import numpy as np
from matplotlib import pylab
import seaborn as sns



spot = 2.45
maturity = 0.25
vol = 0.25
r = 0.05

def call_option_pricer(spot,strike,maturity,r,vol):
    d1 = (log(spot/strike) + (r + 0.5 * vol * vol) * maturity)/vol/sqrt(maturity)
    d2 = d1 - vol * sqrt(maturity)
    price = spot * norm.cdf(d1)-strike * exp(-r * maturity) * norm.cdf(d2)
    return price
# print(call_option_pricer(2.45,2.5,0.25,0.05,0.25))

#use numpy to accelerate
portfolioSize = range(1,10000,500)
timeSpent = []

# #before
for size in portfolioSize:
    now = time.time()
    strikes = np.linspace(2.0,3.0,size)
    for i in range(size):
        res = call_option_pricer(spot, strikes[i], maturity, r, vol)
    timeSpent.append(time.time() - now)


# sns.set(style="ticks")
# pylab.figure(figsize = (12,8))
# pylab.bar(portfolioSize, timeSpent, color = 'r', width =300)
# pylab.grid(True)
# pylab.title('time of calculation (s)',fontsize = 18)
# pylab.ylabel('time（s)', fontsize = 15)
# pylab.xlabel('numbers', fontsize = 15)
# pylab.show()
#
# #all functions in Numpy can apply to a list of number, i.e vectors.
def call_option_pricer_numpy(spot, strike, maturity, r, vol):
    d1 = (np.log(spot/strike) + (r + 0.5 * vol * vol)*maturity)/vol/np.sqrt(maturity)
    d2 = d1 - vol * np.sqrt(maturity)
    price = spot * norm.cdf(d1) - strike * np.exp(-r * maturity) * norm.cdf(d2)
    return price


timeSpentNumpy = []
for size in portfolioSize:
    now = time.time()
    strikes = np.linspace(2.0, 3.0, size)
    res = call_option_pricer_numpy(spot, strikes, maturity, r, vol)
    timeSpentNumpy.append(time.time() - now)

sns.set(style="ticks")
# pylab.figure(figsize = (12,8))
# pylab.bar(portfolioSize, timeSpentNumpy, color = 'r', width =300)
# pylab.grid(True)
# pylab.title('time of calculation_numpy (s)',fontsize = 18)
# pylab.ylabel('time（s)', fontsize = 15)
# pylab.xlabel('numbers', fontsize = 15)
# #pylab.show()

fig = pylab.figure(figsize=(12,8))
ax = fig.gca()
pylab.plot(portfolioSize,np.log10(timeSpent),portfolioSize, np.log10(timeSpentNumpy))  #make multiple line with one commmand
pylab.grid(True) #grid 网格
from matplotlib.ticker import FuncFormatter
# def millions(x, pos):
#     'The two args are the value and tick position'
#     return '$10^{%.0f}$' % (x)
# formatter = FuncFormatter(millions)
# ax.yaxis.set_major_formatter(formatter)
pylab.title('time(s)', fontsize = 18)
pylab.legend(['iterating', 'numpy_version'], loc = 'upper center', ncol = 2)
pylab.ylabel('log10 of time(s)', fontsize = 15)
pylab.xlabel('number',  fontsize = 15)
>>>>>>> origin/master
pylab.show()