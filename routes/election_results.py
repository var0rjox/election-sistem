from flask import Blueprint, render_template
from mocks.election import dict_president, dict_vic, dict_senator

election_results = Blueprint(
    "election_results", __name__, url_prefix="/election_results"
)


@election_results.route("/")
def index():
    # Datos de la vista
    presidents = dict_president
    vices = dict_vic
    senators = dict_senator
    return render_template(
        "election-results.html", presidents=presidents, vices=vices, senators=senators
    )
