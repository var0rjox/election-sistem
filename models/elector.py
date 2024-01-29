class Elector:
    def __init__(self, name, age, ci, address):
        self._name = name
        self._age = age
        self._ci = ci
        self._address = address
        self._state = True

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def ci(self):
        return self._ci

    @property
    def address(self):
        return self._address

    def poll(self, vote, candidate):
        vote.elector = self
        vote.candidate = candidate
        self._state = False

    def __str__(self):
        return f"Voter: {self.name}, Age: {self.age}, Address: {self.address}"
