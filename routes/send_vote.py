from flask import Blueprint
from controllers.vote_controller import vote_controller, send_vote_controller

send_vote = Blueprint("send_vote", __name__)


@send_vote.route("/send_vote")
def vote():
    return send_vote_controller()


@send_vote.route("/submit_vote", methods=["POST"])
def submit_vote():
    return vote_controller()
