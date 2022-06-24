from rng import RNG
from exceptions import InvalidValue
from datetime import datetime
import time

#Linear Feedback Shift Register
class LFSR(RNG):

    def __init__(self, seed = int(time.time())):
        if(seed <= 0):
            raise InvalidValue("seed")
        
        self.__seed = seed
        self.__lfsr = seed

    def setSeed(self, seed):
        if(seed > 0):
            self.__seed = seed
        else:
            raise InvalidValue('seed')

    def getSeed(self):
        return self.__seed

    def random(self, size = None):
        if(size == None):
            return self.__randomOne()
        else:
            return self.__randomArray(size)

    def __randomOne(self):
        lfsr = self.__seed
        bit = (lfsr ^ (lfsr >> 1) ^ (lfsr >> 2) ^ (lfsr >> 22)) & 1
        lfsr = (lfsr >> 1) | (bit << 31)
        return lfsr/4294967296

    def __randomArray(self, size):
        array = []
        lfsr = int((time.time() - int(time.time())) * (1<<31))
        for i in range(size):
            bit = (lfsr ^ (lfsr >> 1) ^ (lfsr >> 2) ^ (lfsr >> 22)) & 1
            lfsr = (lfsr >> 1) | (bit << 31)
            array.append(lfsr/4294967296)
        return array