class Vote:
    def __init__(self, candidate, elector):
        self.__candidate = candidate
        self.__elector = elector

    @property
    def candidate(self):
        return self.__candidate

    @property
    def elector(self):
        return self.__elector
