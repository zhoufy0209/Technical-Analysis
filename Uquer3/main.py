<<<<<<< HEAD
import numpy as np
import math
import seaborn as sns
from matplotlib import pylab



#Jarrow-Rudd binominal tree
ttm = 3.0 # time to maturity
tSteps = 25 # the number of steps
r = 0.03
d = 0.02 # rate of dividend
sigma = 0.2
strike = 100.0
spot = 100.0

dt = ttm/tSteps
up = math.exp((r-d-0.5*sigma*sigma)*dt + sigma*math.sqrt(dt))
down = math.exp((r-d-0.5*sigma*sigma)*dt - sigma*math.sqrt(dt))
discount = math.exp(-r*dt)

# construct the binominal tree

lattice = np.zeros((tSteps+1, tSteps+1))
lattice[0][0] = spot
for i in range(tSteps):
    for j in range(i+1):
        lattice[i+1][j+1] = up*lattice[i][j]
    lattice[i+1][0] = down * lattice[i][0]

pylab.figure(figsize=(12,8))
pylab.plot(lattice[tSteps])
pylab.title('stock price at maturity')
pylab.show()

def call_payoff(spot):
    global strike
    return max((spot - strike),0.0)

pylab.figure(figsize=(12,8))
pylab.plot(list(map(call_payoff, lattice[tSteps])))  #In python 3, map returns a object.
pylab.title('payoff at maturity')
pylab.show()

for i in range (tSteps,0,-1):
    for j in range(i,0,-1):
        if i==tSteps:
            lattice[i-1][j-1] = 0.5*discount*(call_payoff(lattice[i][j])+call_payoff(lattice[i][j-1]))
        else:
            lattice[i-1][j-1] = 0.5*discount*(lattice[i][j]+lattice[i][j-1])


print('the price of call option is %.4f'%lattice[0][0] +'.')

=======
import numpy as np
import math
import seaborn as sns
from matplotlib import pylab



#Jarrow-Rudd binominal tree
ttm = 3.0 # time to maturity
tSteps = 25 # the number of steps
r = 0.03
d = 0.02 # rate of dividend
sigma = 0.2
strike = 100.0
spot = 100.0

dt = ttm/tSteps
up = math.exp((r-d-0.5*sigma*sigma)*dt + sigma*math.sqrt(dt))
down = math.exp((r-d-0.5*sigma*sigma)*dt - sigma*math.sqrt(dt))
discount = math.exp(-r*dt)

# construct the binominal tree

lattice = np.zeros((tSteps+1, tSteps+1))
lattice[0][0] = spot
for i in range(tSteps):
    for j in range(i+1):
        lattice[i+1][j+1] = up*lattice[i][j]
    lattice[i+1][0] = down * lattice[i][0]

pylab.figure(figsize=(12,8))
pylab.plot(lattice[tSteps])
pylab.title('stock price at maturity')
pylab.show()

def call_payoff(spot):
    global strike
    return max((spot - strike),0.0)

pylab.figure(figsize=(12,8))
pylab.plot(list(map(call_payoff, lattice[tSteps])))  #In python 3, map returns a object.
pylab.title('payoff at maturity')
pylab.show()

for i in range (tSteps,0,-1):
    for j in range(i,0,-1):
        if i==tSteps:
            lattice[i-1][j-1] = 0.5*discount*(call_payoff(lattice[i][j])+call_payoff(lattice[i][j-1]))
        else:
            lattice[i-1][j-1] = 0.5*discount*(lattice[i][j]+lattice[i][j-1])


print('the price of call option is %.4f'%lattice[0][0] +'.')

>>>>>>> origin/master
