from models.elector import Elector
from models.vote import Vote
from models.candidate import Candidate

# Electors
electors = []
for i in range(10):
    elector = Elector()
    elector_data = {
        "name": "Elector " + str(i + 1),
        "age": 18 + i,
        "address": "Address " + str(i + 1),
    }
    elector.update_data(elector_data)
    electors.append(elector)

# Candidates

# Votes
