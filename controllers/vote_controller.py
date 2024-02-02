from flask import session, request, render_template, redirect, url_for

from services.vote_service import VoteService
from services.voters_service import VotersServices
from services.db_service import DBService

vote_service = VoteService()
voter_service = VotersServices()
db_service = DBService()


def send_vote_controller():
    political_parties = db_service.get_political_parties()
    return render_template("send-vote.html", candidates=political_parties)


def vote_controller():
    id_political_party = request.form.get("selected_candidate")
    vote_service.add_vote(session["ci"], id_political_party)
    voter_service.update_voter_status(session["ci"])
    return redirect(url_for("home.voter_logout"))
