from datetime import date

class Voter:
    def __init__(self, ci, name, birthdate: date, is_enabled, gender, photo):
        self.ci = ci
        self.name = name
        self.birthdate = birthdate
        self.is_enabled = is_enabled
        self.gender = gender
        self.photo = photo

