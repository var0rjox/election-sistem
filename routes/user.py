from flask import Blueprint, render_template

from models.user import User

user = Blueprint('user', __name__, url_prefix="/user")

@user.route('/')
def index():
    current_user = User('admin', 'root')
    return render_template('user.html', user=current_user)