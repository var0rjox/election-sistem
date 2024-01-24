from flask import Blueprint

vote = Blueprint('vote', __name__, url_prefix="/vote")

@vote.route('/')
def index():
    return 'Hola, aqui es donde se vota'