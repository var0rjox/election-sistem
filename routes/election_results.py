from flask import Blueprint, render_template

from models.result_report import ResultReport
from services.vote_service import VoteService
from services.voters_service import VotersServices

election_results = Blueprint(
    "election_results", __name__, url_prefix="/resultados-elecciones"
)


@election_results.route("/")
def index():
    result_report = ResultReport()
    vote_service = VoteService()
    voters_service = VotersServices()
    report = result_report.report(vote_service.get_all_votes())
    enabled = len(voters_service.get_all_voters())

    return render_template(
        "election-results.html",
        enabled=enabled,
        votes=report["total"],
        political_parties=report["totalPoliticalParties"],
        details=report["details"],
    )
