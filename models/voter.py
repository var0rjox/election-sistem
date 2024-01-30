from datetime import date
from .person import Person


class Voter(Person):
    def __init__(self, ci, name, birthdate: date, gender, photo, is_enabled=True):
        super().__init__(ci, name, birthdate, gender, photo)
        self.__is_enabled = is_enabled

    @property
    def is_enabled(self):
        return self.__is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        self.__is_enabled = is_enabled
