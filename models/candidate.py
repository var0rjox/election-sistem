class Candidate:
    def __init__(self, name, position, political_party):
        self.__name = name
        self.__position = position
        self.__political_party = political_party

    def __str__(self):
        return f"Candidate: {self.name}, Cargo: {self.position}, Partido: {self.political_party}"

    @property
    def get_name(self):
        return self.__name

    @property
    def get_position(self):
        return self.__position

    @property
    def get_political_party(self):
        return self.__political_party
