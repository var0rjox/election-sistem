from services.db_service import DBService

db_service = DBService()


class VotersServices:
    def get_single_voter(self, ci):
        voter = db_service.get_voter(ci)
        return voter

    def get_all_voters(self):
        self.voters = db_service.get_voters()
        return self.voters

    def update_voter_status(self, ci):
        db_service.update_voter_enabled(ci, False)

        return True
