class ResultReport:
    def report(self, results):
        report = {}
        report["total"] = len(results)
        report["details"] = {}
        for vote in results:
            if vote.candidate_voted in report["details"]:
                report["details"][vote.candidate_voted] += 1
            else:
                report["details"][vote.candidate_voted] = 1

        return report
