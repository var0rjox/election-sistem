from .candidate import Candidate


class PoliticalParty:
    def __init__(self, name, acronym, logo, description="", representative=None):
        self.__name = name
        self.__acronym = acronym
        self.__logo = logo
        self.__description = description
        self.__candidates: list[Candidate] = []
        self.__representative: Candidate = representative

    @property
    def name(self):
        return self.__name

    @property
    def acronym(self):
        return self.__acronym

    @property
    def logo(self):
        return self.__logo

    @property
    def candidates(self):
        return self.__candidates

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    def add_candidate(self, candidate: Candidate):
        self.__candidates.append(candidate)

    @property
    def representative(self):
        return self.__representative

    @representative.setter
    def representative(self, representative):
        self.__representative = representative
