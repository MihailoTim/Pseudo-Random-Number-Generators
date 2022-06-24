class InvalidValue(Exception):

    def __init__(self, variableName):
        self.__variableName = variableName

    def __str__(self):
        return f'Invalid value for {self.__variableName}\n'