from flask import Blueprint
from controllers.voter_controller import voter_load_information

voter = Blueprint("voter", __name__, url_prefix="/perfil-elector")


@voter.route("/")
def index():
    return voter_load_information()
