from flask import Blueprint, render_template
from .forms import Login

electoral_committee = Blueprint('electoral_committee', __name__, url_prefix='/comite-electoral', template_folder='../../templates')

@electoral_committee.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    return render_template('committee_login.html', form = form)