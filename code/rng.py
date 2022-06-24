class RNG:
    def __init__(self, seed = 0):
        self._seed = seed

    def setSeed(self, s):
        self._seed = s

    def getSeed(self):
        return self._seed

    def random(self):
        raise NotImplementedError()