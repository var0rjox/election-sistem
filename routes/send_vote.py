from flask import Blueprint
from controllers.vote_controller import vote_controller, send_vote_controller

send_vote = Blueprint("send_vote", __name__)


@send_vote.route("/enviar_voto")
def vote():
    return send_vote_controller()


@send_vote.route("/subir_voto", methods=["POST"])
def submit_vote():
    return vote_controller()
