<<<<<<< HEAD
import scipy
import numpy as np
from scipy.stats import norm
from math import log, sqrt, exp
from matplotlib import pylab
import seaborn as sns
import time
from scipy.optimize import brentq

spot = 2.45
maturity = 0.25
strike = 2.50
vol = 0.25
r = 0.05

# pylab.figure(figsize = (12,8))
# randomSeires = scipy.random.randn(10000)
# pylab.plot(randomSeires)
# pylab.xlim(-1,10000)
# pylab.ylim(-4,5)
# pylab.text(-0.8, 4.5, 'mean: %.4f' % randomSeires.mean() +' '+ 'std: %.4f' % randomSeires.std())
# pylab.show()


#calculate option price in Monte Carlo Way

def call_option_pricer(spot,strike,maturity,r,vol):
    d1 = (log(spot/strike) + (r + 0.5 * vol * vol) * maturity)/vol/sqrt(maturity)
    d2 = d1 - vol * sqrt(maturity)
    price = spot * norm.cdf(d1)-strike * exp(-r * maturity) * norm.cdf(d2)
    return price


def call_option_pricer_monte_carlo(spot, strike, maturity, r, vol, N = 10000):
    randomSeries = scipy.random.randn(N)
    s_t = spot * np.exp((r + 0.5 * vol * vol) * maturity +randomSeries * vol * np.sqrt(maturity))
    sum_Value = np.maximum((s_t - strike), 0 ).sum()
    price = np.exp(-r * maturity) * sum_Value / N
    return price


#print('the price of call opiton is %.4f' % call_option_pricer_monte_carlo(spot, strike, maturity, r, vol, N = 10000))

# pathScenario = range (1000, 100000, 1000)
# number_of_trial = 100
# CIUpper = []
# CILower = []
# means = []
# for scenario in pathScenario:
#     res = np.zeros(number_of_trial)
#     for i in range(number_of_trial):
#         res[i] = call_option_pricer_monte_carlo(spot, strike, maturity, r, vol, N = scenario)
#     means.append(res.mean())
#     CILower.append(res.mean() - 1.96 * res.std())
#     CIUpper.append(res.mean() + 1.96 * res.std())
#
# pylab.figure(figsize=(12, 8))
# table = np.array([means,CIUpper,CILower]).T
# pylab.plot(pathScenario, table)
# pylab.title('price a option in MC method', fontsize = 18)
# pylab.legend(['means','upper bound', 'lower bound'],loc = 'upper left')
# pylab.ylabel('price',fontsize = 15)
# pylab.xlabel('numbers of simulation', fontsize = 15)
# pylab.grid(True)
# pylab.show()





class cost_function:  #如果在创建class的时候写了call（）方法， 那么该class实例化出实例后， 实例名()就是调用call（）方法
    def __init__(self,target):
        self.targetValue = target

    def __call__(self, x):
        return call_option_pricer(spot,strike,maturity,r,x) - self.targetValue

target = call_option_pricer(spot=2.45, strike=2.5, maturity=0.25, r=0.05, vol=0.25)
cost_sampel = cost_function(target)

impliedVol = brentq((cost_sampel), 0.005, 0.05)

print('implied volatility : %.2f' % (impliedVol * 100) + '%')

=======
import scipy
import numpy as np
from scipy.stats import norm
from math import log, sqrt, exp
from matplotlib import pylab
import seaborn as sns
import time
from scipy.optimize import brentq

spot = 2.45
maturity = 0.25
strike = 2.50
vol = 0.25
r = 0.05

# pylab.figure(figsize = (12,8))
# randomSeires = scipy.random.randn(10000)
# pylab.plot(randomSeires)
# pylab.xlim(-1,10000)
# pylab.ylim(-4,5)
# pylab.text(-0.8, 4.5, 'mean: %.4f' % randomSeires.mean() +' '+ 'std: %.4f' % randomSeires.std())
# pylab.show()


#calculate option price in Monte Carlo Way

def call_option_pricer(spot,strike,maturity,r,vol):
    d1 = (log(spot/strike) + (r + 0.5 * vol * vol) * maturity)/vol/sqrt(maturity)
    d2 = d1 - vol * sqrt(maturity)
    price = spot * norm.cdf(d1)-strike * exp(-r * maturity) * norm.cdf(d2)
    return price


def call_option_pricer_monte_carlo(spot, strike, maturity, r, vol, N = 10000):
    randomSeries = scipy.random.randn(N)
    s_t = spot * np.exp((r + 0.5 * vol * vol) * maturity +randomSeries * vol * np.sqrt(maturity))
    sum_Value = np.maximum((s_t - strike), 0 ).sum()
    price = np.exp(-r * maturity) * sum_Value / N
    return price


#print('the price of call opiton is %.4f' % call_option_pricer_monte_carlo(spot, strike, maturity, r, vol, N = 10000))

# pathScenario = range (1000, 100000, 1000)
# number_of_trial = 100
# CIUpper = []
# CILower = []
# means = []
# for scenario in pathScenario:
#     res = np.zeros(number_of_trial)
#     for i in range(number_of_trial):
#         res[i] = call_option_pricer_monte_carlo(spot, strike, maturity, r, vol, N = scenario)
#     means.append(res.mean())
#     CILower.append(res.mean() - 1.96 * res.std())
#     CIUpper.append(res.mean() + 1.96 * res.std())
#
# pylab.figure(figsize=(12, 8))
# table = np.array([means,CIUpper,CILower]).T
# pylab.plot(pathScenario, table)
# pylab.title('price a option in MC method', fontsize = 18)
# pylab.legend(['means','upper bound', 'lower bound'],loc = 'upper left')
# pylab.ylabel('price',fontsize = 15)
# pylab.xlabel('numbers of simulation', fontsize = 15)
# pylab.grid(True)
# pylab.show()





class cost_function:  #如果在创建class的时候写了call（）方法， 那么该class实例化出实例后， 实例名()就是调用call（）方法
    def __init__(self,target):
        self.targetValue = target

    def __call__(self, x):
        return call_option_pricer(spot,strike,maturity,r,x) - self.targetValue

target = call_option_pricer(spot=2.45, strike=2.5, maturity=0.25, r=0.05, vol=0.25)
cost_sampel = cost_function(target)

impliedVol = brentq((cost_sampel), 0.005, 0.05)

print('implied volatility : %.2f' % (impliedVol * 100) + '%')

>>>>>>> origin/master
