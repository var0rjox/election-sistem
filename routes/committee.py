from flask import Blueprint
from controllers.comittee_controller import (
    login_controller,
    profile_controller,
    logout_controller,
)

electoral_committee = Blueprint(
    "electoral_committee",
    __name__,
    url_prefix="/comite-electoral",
    template_folder="../../templates",
)


@electoral_committee.route("/login", methods=["GET", "POST"])
def login():
    return login_controller()


@electoral_committee.route("/perfil")
def profile():
    return profile_controller()


@electoral_committee.route("/logout")
def logout():
    return logout_controller()
