from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.validators import InputRequired, Length

class Login(FlaskForm):
    ci = PasswordField('CI', validators=[InputRequired(), Length(min=7, max=10)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=12)])