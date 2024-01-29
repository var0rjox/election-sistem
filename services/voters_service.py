import datetime
from models.voter import Voter


class VotersServices:
    voters = [
        Voter(
            ci="1234567",
            birthdate=datetime.date(2002, 5, 5),
            is_enabled=True,
            name="Juan Perez",
            gender="Male",
            photo="https://picsum.photos/200/300",
        ),
        Voter(
            ci="7654321",
            birthdate=datetime.date(1990, 1, 1),
            is_enabled=True,
            name="Maria Perez",
            gender="Female",
            photo="https://picsum.photos/200/300",
        ),
        Voter(
            ci="1234567",
            birthdate=datetime.date(2002, 5, 5),
            is_enabled=True,
            name="Juan Perez",
            gender="Male",
            photo="https://picsum.photos/200/300",
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

    def update_voter_status(self, ci):
        for voter in self.voters:
            if voter.ci == ci:
                voter.is_enabled = not voter.is_enabled
                return voter

        return None
