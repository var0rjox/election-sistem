from datetime import date


class Voter:
    def __init__(self, ci, birthdate: date, is_enabled, name):
        self.ci = ci
        self.birthdate = birthdate
        self.is_enabled = is_enabled
        self.name = name
