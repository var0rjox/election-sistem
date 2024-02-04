from flask import render_template
from utils.create_pie_diagram import create_pie_diagram

from models.result_report import ResultReport
from services.vote_service import VoteService
from services.voters_service import VotersServices


def results_controller():
    result_report = ResultReport()
    vote_service = VoteService()
    voters_service = VotersServices()

    results = vote_service.get_all_votes()
    report = result_report.report(results)
    enabled = len(voters_service.get_all_voters())
    json_diagram = create_pie_diagram(results)

    return render_template(
        "election-results.html",
        enabled=enabled,
        votes=report["total"],
        political_parties=report["totalPoliticalParties"],
        details=report["details"],
        json_diagram=json_diagram,
    )
