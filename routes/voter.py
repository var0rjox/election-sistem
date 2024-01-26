from flask import Blueprint, render_template
from models.voter import Voter

voter = Blueprint('voter', __name__, url_prefix="/voter-perfil")

@voter.route('/')
def index():
    current_voter = Voter('9394750','Emerson Denis Vera Viscarra','20/10/1999', True,'Masculino', 'Foto')
    return render_template('profile.html', voter=current_voter)
