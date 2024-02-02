from services.db_service import DBService

db_service = DBService()


class VoteService:
    def add_vote(self, voter_ci, political_party_id):
        db_service.add_vote(voter_id=voter_ci, political_party_id=political_party_id)

    def get_all_votes(self):
        votes = db_service.get_votes()
        return votes
