class Mouse:
    def __init__(self, name, sensevity):
        self.__name = name
        self.__sensevity = sensevity

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_sensevity(self):
        return self.__sensevity

    def set_sensevity(self, sensevity):
        self.__sensevity = sensevity

    def getinfo(self):
        return self.__name, self.__sensevity
