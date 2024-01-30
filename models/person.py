from datetime import date


class Person:
    def __init__(self, ci, name, birthdate: date, gender, photo):
        self.__ci = ci
        self.__name = name
        self.__birthdate = birthdate
        self.__gender = gender
        self.__photo = photo

    @property
    def ci(self):
        return self.__ci

    @property
    def name(self):
        return self.__name

    @property
    def birthdate(self):
        return self.__birthdate

    @property
    def gender(self):
        return self.__gender

    @property
    def photo(self):
        return self.__photo
