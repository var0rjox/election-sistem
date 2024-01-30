from mocks.voters import voters


class VotersServices:
    def __init__(self):
        self.voters = voters

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
