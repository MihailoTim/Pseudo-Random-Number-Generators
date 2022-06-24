from rng import RNG
from exceptions import InvalidValue
from datetime import datetime
import time

class LCG(RNG):

    #criteria for parameter selection:
    #c and m to be coprime
    #all prime factors of m divide a-1
    #if m is multiple of 4, then a-1 is multiple of 4
    #predefined values for moduo, increment and multiplier are based on Donald Knuth's recommendations
    def __init__(self, seed = int(time.time()), moduo = 4294967296, increment = 907633385, multiplier = 429493445):
        if(moduo < seed or  moduo < increment or moduo < multiplier):
            raise InvalidValue("moduo")
        if(seed < 0):
            raise InvalidValue("seed")
        if(increment < 0):
            raise InvalidValue("increment")
        if(multiplier < 0):
            raise InvalidValue("multiplier")
            
        self.__seed = seed
        self.__moduo = moduo
        self.__increment = increment
        self.__multiplier = multiplier

    def setSeed(self, seed):
        if(0 <= seed < self.__moduo):
            self.__seed = seed
        else:
            raise InvalidValue('seed')

    def getSeed(self):
        return self.__seed

    def setModuo(self, moduo):
        if(0 < moduo and moduo > self.__seed and moduo > self.__multiplier and moduo > self.__increment):
            self.__moduo = moduo
        else:
            raise InvalidValue('moduo')

    def getModuo(self):
        return self.__moduo

    def setIncrement(self, increment):
        if(0 <= increment < self.__moduo):
            self.__increment = increment
        else:
            raise InvalidValue('increment')

    def getIncrement(self):
        return self.__increment

    def setMultiplier(self, multiplier):
        if(0 <= multiplier < self.__moduo):
            self.__multiplier = multiplier
        else:
            raise InvalidValue('multiplier')

    def getMultiplier(self):
        return self.__multiplier

    def random(self, size = None):
        if(size == None):
            return self.__randomOne()
        else:
            return self.__randomArray(size)

    def __randomArray(self, size):
        array = []
        for i in range(size):
            array.append(self.random())
        return array

    def __randomOne(self):
        self.__seed = (self.__multiplier * self.__seed + self.__increment) % self.__moduo
        return self.__seed/4294967296
