from mocks.political_parties import political_parties


class ResultReport:
    def report(self, results):
        report = {}
        report["total"] = len(results)
        report["details"] = {}
        report["totalPoliticalParties"] = len(political_parties)

        for party in political_parties:
            report["details"][party.name] = {"votes": 0, "percentage": 0, "data": party}

        report["details"]["Nulo"] = {"votes": 0, "percentage": 0, "data": None}
        report["details"]["Blanco"] = {"votes": 0, "percentage": 0, "data": None}

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
