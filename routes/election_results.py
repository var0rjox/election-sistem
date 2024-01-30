from flask import Blueprint

from controllers.results_controller import results_controller

election_results = Blueprint("election_results", __name__)


@election_results.route("/resultados-elecciones")
def index():
    return results_controller()
