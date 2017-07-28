<<<<<<< HEAD
import math
import numpy as np
import scipy.stats

def call_option_pricer(spot,strike,maturity,r,vol):
    d1 = (math.log(spot/strike) + (r + 0.5 * vol * vol) * maturity)/vol/math.sqrt(maturity)
    d2 = d1 - vol * math.sqrt(maturity)
    price = spot * scipy.stats.norm.cdf(d1)-strike * math.exp(-r * maturity) * scipy.stats.norm.cdf(d2)
    return price

class BinominalTree:
    def __init__(self,spot,strike, riskFree,dividend,tSteps,maturity,sigma,treeTraits):    # 'treeTraits' is a class.
        self.dt = maturity/tSteps
        self.spot = spot
        self.strike = strike
        self.r = riskFree
        self.d = dividend
        self.tSteps = tSteps
        self.discount = math.exp(-self.r * self.dt)
        self.v = sigma
        self.up = treeTraits.up(self)
        self.down = treeTraits.down(self)
        self.upProbability = treeTraits.upProbability(self)
        self.downProbability = 1.0 - self.upProbability
        self._build_lattice()

    def _build_lattice(self):  # _ before the name of function declares it privacy.
        '''
        building a binominal tree
        '''
        self.lattice = np.zeros((self.tSteps+1,self.tSteps+1))
        self.lattice[0][0] = self.spot
        for i in range(self.tSteps):
            for j in range(i+1):
                self.lattice[i+1][j+1] = self.up*self.lattice[i][j]
            self.lattice[i+1][0] = self.down*self.lattice[i][0]

    def roll_back(self, payoff):
        for i in range(self.tSteps,0,-1):
            for j in range(i,0,-1):
                if i == self.tSteps:
                    self.lattice[i-1][j-1] = self.discount * (
                        self.upProbability*payoff(self.strike,self.lattice[i][j])+self.downProbability*payoff(self.strike,
                            self.lattice[i][j-1]))
                else:
                    self.lattice[i - 1][j - 1] = self.discount * (
                        self.upProbability * self.lattice[i][j] + self.downProbability * self.lattice[i][j - 1])



class JarrowRuddTraits:
    '''
    Static methods are a special case of methods. Sometimes, you'll write code that belongs to a class,
    but that doesn't use the object itself at all. In JarrowRuddTraits, none of its attributes is used.
    Static methods help us avoid to initialize a object.
    '''
    @staticmethod
    def up(tree):
        return math.exp((tree.r - tree.d - 0.5 * tree.v * tree.v) * tree.dt + tree.v * math.sqrt(tree.dt))

    @staticmethod
    def down(tree):
        return math.exp((tree.r - tree.d - 0.5 * tree.v * tree.v) * tree.dt - tree.v * math.sqrt(tree.dt))

    @staticmethod
    def upProbability(tree):
        return 0.5


class CRRTraits:
    @staticmethod
    def up(tree):
        return math.exp(tree.v * math.sqrt(tree.dt))

    @staticmethod
    def down(tree):
        return math.exp(-tree.v * math.sqrt(tree.dt))

    @staticmethod
    def upProbability(tree):
        return 0.5 + 0.5 * (tree.r - tree.d - 0.5 * tree.v * tree.v) * tree.dt / tree.v / math.sqrt(tree.dt)

def pay_off(strike, spot):
   return max(spot - strike, 0.0)




class ExtendBinominal(BinominalTree):
    def roll_back_american(self,payoff):
        for i in range(self.tSteps, 0, -1):
            for j in range(i, 0, -1):
                if i == self.tSteps:
                    europeanValue = self.discount * (
                        self.upProbability * payoff(self.strike,self.lattice[i][j])
                        + self.downProbability * payoff(self.strike,self.lattice[i][j - 1]))
                else:
                    europeanValue = self.discount * (
                        self.upProbability * self.lattice[i][j] + self.downProbability * self.lattice[i][j - 1])
                exerciseValue = pay_off(self.strike,self.lattice[i-1][j-1])
                self.lattice[i-1][j-1] = max(exerciseValue,europeanValue)
=======
import math
import numpy as np
import scipy.stats

def call_option_pricer(spot,strike,maturity,r,vol):
    d1 = (math.log(spot/strike) + (r + 0.5 * vol * vol) * maturity)/vol/math.sqrt(maturity)
    d2 = d1 - vol * math.sqrt(maturity)
    price = spot * scipy.stats.norm.cdf(d1)-strike * math.exp(-r * maturity) * scipy.stats.norm.cdf(d2)
    return price

class BinominalTree:
    def __init__(self,spot,strike, riskFree,dividend,tSteps,maturity,sigma,treeTraits):    # 'treeTraits' is a class.
        self.dt = maturity/tSteps
        self.spot = spot
        self.strike = strike
        self.r = riskFree
        self.d = dividend
        self.tSteps = tSteps
        self.discount = math.exp(-self.r * self.dt)
        self.v = sigma
        self.up = treeTraits.up(self)
        self.down = treeTraits.down(self)
        self.upProbability = treeTraits.upProbability(self)
        self.downProbability = 1.0 - self.upProbability
        self._build_lattice()

    def _build_lattice(self):  # _ before the name of function declares it privacy.
        '''
        building a binominal tree
        '''
        self.lattice = np.zeros((self.tSteps+1,self.tSteps+1))
        self.lattice[0][0] = self.spot
        for i in range(self.tSteps):
            for j in range(i+1):
                self.lattice[i+1][j+1] = self.up*self.lattice[i][j]
            self.lattice[i+1][0] = self.down*self.lattice[i][0]

    def roll_back(self, payoff):
        for i in range(self.tSteps,0,-1):
            for j in range(i,0,-1):
                if i == self.tSteps:
                    self.lattice[i-1][j-1] = self.discount * (
                        self.upProbability*payoff(self.strike,self.lattice[i][j])+self.downProbability*payoff(self.strike,
                            self.lattice[i][j-1]))
                else:
                    self.lattice[i - 1][j - 1] = self.discount * (
                        self.upProbability * self.lattice[i][j] + self.downProbability * self.lattice[i][j - 1])



class JarrowRuddTraits:
    '''
    Static methods are a special case of methods. Sometimes, you'll write code that belongs to a class,
    but that doesn't use the object itself at all. In JarrowRuddTraits, none of its attributes is used.
    Static methods help us avoid to initialize a object.
    '''
    @staticmethod
    def up(tree):
        return math.exp((tree.r - tree.d - 0.5 * tree.v * tree.v) * tree.dt + tree.v * math.sqrt(tree.dt))

    @staticmethod
    def down(tree):
        return math.exp((tree.r - tree.d - 0.5 * tree.v * tree.v) * tree.dt - tree.v * math.sqrt(tree.dt))

    @staticmethod
    def upProbability(tree):
        return 0.5


class CRRTraits:
    @staticmethod
    def up(tree):
        return math.exp(tree.v * math.sqrt(tree.dt))

    @staticmethod
    def down(tree):
        return math.exp(-tree.v * math.sqrt(tree.dt))

    @staticmethod
    def upProbability(tree):
        return 0.5 + 0.5 * (tree.r - tree.d - 0.5 * tree.v * tree.v) * tree.dt / tree.v / math.sqrt(tree.dt)

def pay_off(strike, spot):
   return max(spot - strike, 0.0)




class ExtendBinominal(BinominalTree):
    def roll_back_american(self,payoff):
        for i in range(self.tSteps, 0, -1):
            for j in range(i, 0, -1):
                if i == self.tSteps:
                    europeanValue = self.discount * (
                        self.upProbability * payoff(self.strike,self.lattice[i][j])
                        + self.downProbability * payoff(self.strike,self.lattice[i][j - 1]))
                else:
                    europeanValue = self.discount * (
                        self.upProbability * self.lattice[i][j] + self.downProbability * self.lattice[i][j - 1])
                exerciseValue = pay_off(self.strike,self.lattice[i-1][j-1])
                self.lattice[i-1][j-1] = max(exerciseValue,europeanValue)
>>>>>>> origin/master
