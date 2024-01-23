from flask import Blueprint, render_template

from models.elector import Elector

elector = Blueprint('elector', __name__, url_prefix="/elector")

@elector.route('/')
def index():
    current_elector = Elector('9394750','Emerson','20/10/1999','Masculino')
    return render_template('profile.html', elector=current_elector)