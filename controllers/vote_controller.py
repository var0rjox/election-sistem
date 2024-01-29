from flask import session, request, render_template, redirect, url_for

from services.vote_service import VoteService
from services.voters_service import VotersServices
from mocks.political_partys import political_partys

vote_service = VoteService()
voter_service = VotersServices()


def send_vote_controller():
    return render_template("send-vote.html", candidates=political_partys)


def vote_controller():
    candidate = request.form.get("selected_candidate")
    vote_service.add_vote(session["ci"], candidate)
    voter_service.update_voter_status(session["ci"])
    return redirect(url_for("home.voter_logout"))
