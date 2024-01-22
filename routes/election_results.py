from flask import Blueprint, render_template

# from models.user import User

election_results = Blueprint('election_results', __name__, url_prefix="/election_results")

@election_results.route('/')
def index():
    return render_template('election_results.html')