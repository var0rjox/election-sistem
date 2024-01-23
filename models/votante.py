class Votante:
  def __init__(self, name, age, ci, address):
    self.name = name
    self.age = age
    self.ci = ci
    self.address = address
    self._state = True

  def update_address(self, new_address):
    self.address = new_address

  def votar(self, candidatos):
    for candidato in candidatos:
      if candidato.name == self.name:
        candidato.votos += 1
      print(candidatos)
    self._state = False

  def __str__(self):
    return f"Voter: {self.name}, Age: {self.age}, Address: {self.address}"

class Candidato:
    def __init__(self, name, cargo, partido):
        self.name = name
        self.cargo = cargo
        self.partido = partido
        self.votos = 0

    def __str__(self):
        return f"Candidate: {self.name}, Cargo: {self.cargo}, Partido: {self.partido}, Votes: {self.votos}"


class Cargo:
  def __init__(self, name):
    self.name = name
    self.candidatos = []

  def add_candidato(self, candidato):
    self.candidatos.append(candidato)

  def __str__(self):
    return f"Cargo: {self.name}, Candidatos: {', '.join(c.name for c in self.candidatos)}"
