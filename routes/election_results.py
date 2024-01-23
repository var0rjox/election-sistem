from flask import Blueprint, render_template

from models.votante import Votante , Cargo , Candidato

election_results = Blueprint('election_results', __name__, url_prefix="/election_results")

@election_results.route('/')
def index():
      # Datos de la vista
    return render_template('election_results.html')