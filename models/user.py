from datetime import date
from .person import Person


class User(Person):
    def __init__(self, ci, name, birthdate: date, gender, photo, password):
        super().__init__(ci, name, birthdate, gender, photo)
        self.__password = password

    @property
    def password(self):
        return self.__password
