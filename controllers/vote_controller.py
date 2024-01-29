from services.vote_service import VoteService
from flask import session, request, render_template, redirect, url_for
from mocks.candidates import candidates

vote_service = VoteService()


def send_vote_controller():
    return render_template("send_vote.html", candidates=candidates)


def vote_controller():
    candidate = request.form.get("selected_candidate")
    vote_service.add_vote(session["ci"], candidate)
    session["is_enabled"] = False
    return redirect(url_for("home.voter_logout"))
