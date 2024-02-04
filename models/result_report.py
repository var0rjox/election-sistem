from services.db_service import DBService


class ResultReport:
    def __init__(self):
        self.db_service = DBService()

    def report(self, results):
        political_parties = self.db_service.get_political_parties()
        report = {}
        report["total"] = len(results)
        report["details"] = {}
        report["totalPoliticalParties"] = len(political_parties) - 2

        report["details"] = self.getVotesAndPercentages(results)

        for party in political_parties:
            report["details"][party.name]["data"] = party

        return report

    def getDataForPieDiagram(self, results):
        labels = []
        values = []

        votes = self.getVotesAndPercentages(results)

        for party in votes:
            if votes[party]["votes"] > 0:
                labels.append(party)
                values.append(votes[party]["percentage"])

        return {"labels": labels, "values": values}

    def getVotesAndPercentages(self, results):
        total = len(results)
        political_parties = self.db_service.get_political_parties()
        votes = {}
        for party in political_parties:
            votes[party.name] = {"votes": 0, "percentage": 0}

        for vote in results:
            votes[vote.candidate_voted]["votes"] += 1

        for party in votes.values():
            percentage = round(party["votes"] * 100 / total, 2) if total > 0 else 0
            party["percentage"] = percentage

        return votes
