<<<<<<< HEAD
import BinominalTree as BT
from matplotlib import pylab

#Jarrow-Rudd binominal tree
ttm = 3.0 # time to maturity
tSteps = 25 # the number of steps
r = 0.03
d = 0.02  # rate of dividend
sigma = 0.2
strike = 100.0
spot = 100.0

# testTree = BT.BinominalTree(spot,strike,r,d,tSteps,ttm,sigma,BT.JarrowRuddTraits)
# testTree.roll_back(BT.pay_off)
# print(testTree.lattice[0][0])

stepSizes = range(25,500,25)
jrRes = []
crrRes = []

# for i in stepSizes:
#     testTree = BT.BinominalTree(spot,strike,r,d,i,ttm,sigma,BT.JarrowRuddTraits)
#     testTree.roll_back(BT.pay_off)
#     jrRes.append(testTree.lattice[0][0])
#
#     testTree = BT.BinominalTree(spot,strike,r,d,i,ttm,sigma,BT.CRRTeaits)
#     testTree.roll_back(BT.pay_off)
#     crrRes.append(testTree.lattice[0][0])
# anyRes = [BT.call_option_pricer(spot,strike,ttm,r,sigma)]*len(stepSizes)
# pylab.figure(figsize=(16,8))
# pylab.plot(stepSizes, jrRes, '-.', marker = 'o', markersize = 10)
# pylab.plot(stepSizes, crrRes, '-.', marker = 'd', markersize = 10)
# pylab.plot(stepSizes, anyRes, '--')
# pylab.legend(['Jarrow - Rudd', 'Cox - Ross - Rubinstein', 'anlytical'])
# pylab.xlabel('number of steps' )
# pylab.title('convergence', fontsize = 20)
# pylab.grid(True)
# pylab.show()

for i in stepSizes:
    testTree = BT.ExtendBinominal(spot,strike,r,d,i,ttm,sigma,BT.JarrowRuddTraits)
    testTree.roll_back_american(BT.pay_off)
    jrRes.append(testTree.lattice[0][0])

    testTree = BT.ExtendBinominal(spot,strike,r,d,i,ttm,sigma,BT.CRRTraits)
    testTree.roll_back_american(BT.pay_off)
    crrRes.append(testTree.lattice[0][0])
pylab.figure(figsize=(16,8))
pylab.plot(stepSizes, jrRes, '-.', marker = 'o', markersize = 10)
pylab.plot(stepSizes, crrRes, '-.', marker = 'd', markersize = 10)
pylab.legend(['Jarrow - Rudd', 'Cox - Ross - Rubinstein', 'anlytical'])
pylab.xlabel('number of steps' )
pylab.title('convergence', fontsize = 20)
pylab.grid(True)
=======
import BinominalTree as BT
from matplotlib import pylab

#Jarrow-Rudd binominal tree
ttm = 3.0 # time to maturity
tSteps = 25 # the number of steps
r = 0.03
d = 0.02  # rate of dividend
sigma = 0.2
strike = 100.0
spot = 100.0

# testTree = BT.BinominalTree(spot,strike,r,d,tSteps,ttm,sigma,BT.JarrowRuddTraits)
# testTree.roll_back(BT.pay_off)
# print(testTree.lattice[0][0])

stepSizes = range(25,500,25)
jrRes = []
crrRes = []

# for i in stepSizes:
#     testTree = BT.BinominalTree(spot,strike,r,d,i,ttm,sigma,BT.JarrowRuddTraits)
#     testTree.roll_back(BT.pay_off)
#     jrRes.append(testTree.lattice[0][0])
#
#     testTree = BT.BinominalTree(spot,strike,r,d,i,ttm,sigma,BT.CRRTeaits)
#     testTree.roll_back(BT.pay_off)
#     crrRes.append(testTree.lattice[0][0])
# anyRes = [BT.call_option_pricer(spot,strike,ttm,r,sigma)]*len(stepSizes)
# pylab.figure(figsize=(16,8))
# pylab.plot(stepSizes, jrRes, '-.', marker = 'o', markersize = 10)
# pylab.plot(stepSizes, crrRes, '-.', marker = 'd', markersize = 10)
# pylab.plot(stepSizes, anyRes, '--')
# pylab.legend(['Jarrow - Rudd', 'Cox - Ross - Rubinstein', 'anlytical'])
# pylab.xlabel('number of steps' )
# pylab.title('convergence', fontsize = 20)
# pylab.grid(True)
# pylab.show()

for i in stepSizes:
    testTree = BT.ExtendBinominal(spot,strike,r,d,i,ttm,sigma,BT.JarrowRuddTraits)
    testTree.roll_back_american(BT.pay_off)
    jrRes.append(testTree.lattice[0][0])

    testTree = BT.ExtendBinominal(spot,strike,r,d,i,ttm,sigma,BT.CRRTraits)
    testTree.roll_back_american(BT.pay_off)
    crrRes.append(testTree.lattice[0][0])
pylab.figure(figsize=(16,8))
pylab.plot(stepSizes, jrRes, '-.', marker = 'o', markersize = 10)
pylab.plot(stepSizes, crrRes, '-.', marker = 'd', markersize = 10)
pylab.legend(['Jarrow - Rudd', 'Cox - Ross - Rubinstein', 'anlytical'])
pylab.xlabel('number of steps' )
pylab.title('convergence', fontsize = 20)
pylab.grid(True)
>>>>>>> origin/master
pylab.show()