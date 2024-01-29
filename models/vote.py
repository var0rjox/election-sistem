class Vote:
    def __init__(self, elector_ci, candidate_voted, date_voted):
        self.__elector_ci = elector_ci
        self.__candidate_voted = candidate_voted
        self.__date_voted = date_voted

    @property
    def elector_ci(self):
        return self.__elector_ci

    @property
    def candidate_voted(self):
        return self.__candidate_voted

    @property
    def date_voted(self):
        return self.__date_voted
