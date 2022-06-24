from rng import RNG
from exceptions import InvalidValue
import time

#Blum Blum Shub Generator
class BBS(RNG):

    def __init__(self, seed = int(time.time()), moduo = 429497053):

        RNG.__init__(self, seed)

        if(seed<0):
            raise InvalidValue("seed")
        if(moduo<=0):
            raise InvalidValue("moduo")

        self.__seed = seed
        self.__moduo = moduo


    def setSeed(self, seed):
        if(0 <= seed < self.__moduo):
            self.__seed = seed
        else:
            raise InvalidValue('seed')

    def getSeed(self):
        return self.__seed    

    def setModuo(self, moduo):
        if(moduo>0):
            self.__moduo = moduo
        else:
            raise InvalidValue('moduo')

    def getModuo(self):
        return self.__moduo

    def __getParityBit(self, number):
        parity = False
        while(number):
            c = number & 1
            number = number >> 1
            parity = not parity if c==1 else parity
        return 1 if parity else 0

    def __computeNumber(self):
        newNumber = 0
        #32 iteration to get 32 bits
        for i in range(32):
            self.__seed = (self.__seed ** 2) % self.__moduo
            bit = self.__getParityBit(self.__seed)
            newNumber = (newNumber<<1) | bit
        return newNumber

    def random(self, size = None):
        if(size == None):
            return self.__randomOne()
        else:
            return self.__randomArray(size)
        
    def __randomOne(self):
        return self.__computeNumber()/4294967296

    def __randomArray(self, size):
        array = []
        for i in range(size):
            array.append(self.__randomOne())
        return array
    