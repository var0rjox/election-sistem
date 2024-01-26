import datetime
from models.voter import Voter


class VotersServices:
    voters = [
        Voter(
            ci="1234567",
            birthdate=datetime.date(2002, 5, 5),
            is_enabled=True,
            name="Juan Perez",
        ),
        Voter(
            ci="7654321",
            birthdate=datetime.date(1990, 1, 1),
            is_enabled=True,
            name="Maria Perez",
        ),
        Voter(
            ci="1234567",
            birthdate=datetime.date(2002, 5, 5),
            is_enabled=True,
            name="Juan Perez",
        ),
    ]

    def get_single_voter(self, ci):
        for voter in self.voters:
            if voter.ci == ci:
                return voter

        return None

    def get_all_voters(self):
        return self.voters

    def add_voter(self, voter):
        self.voters.append(voter)
