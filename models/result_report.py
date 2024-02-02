from services.db_service import DBService

db_service = DBService()


class ResultReport:
    def report(self, results):
        political_parties = db_service.get_political_parties()
        report = {}
        report["total"] = len(results)
        report["details"] = {}
        report["totalPoliticalParties"] = len(political_parties) - 2

        for party in political_parties:
            report["details"][party.name] = {"votes": 0, "percentage": 0, "data": party}

        for vote in results:
            report["details"][vote.candidate_voted]["votes"] += 1

        for party in report["details"]:
            percentage = (
                round(report["details"][party]["votes"] * 100 / report["total"], 2)
                if report["total"] > 0
                else 0
            )
            report["details"][party]["percentage"] = percentage

        return report
