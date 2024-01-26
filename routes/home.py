from flask import Blueprint

from controllers.home_controller import (
    login_controller,
    voter_profile_controller,
    voter_logout_controller,
)

from services.voters_service import VotersServices

home = Blueprint("home", __name__)

votersService = VotersServices()


@home.route("/", methods=["GET", "POST"])
def login():
    return login_controller()


@home.route("/perfil-votante")
def voter_profile():
    return voter_profile_controller()


@home.route("/voter-logout")
def voter_logout():
    return voter_logout_controller()
