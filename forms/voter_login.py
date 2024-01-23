from flask_wtf import FlaskForm
from wtforms import PasswordField, DateField, SubmitField, ValidationError
from wtforms.validators import InputRequired, Length

from utils.validate_adult import validate_adult


class VoterLogin(FlaskForm):
    ci = PasswordField(
        "Carnet de identidad",
        validators=[
            InputRequired(),
            Length(min=6, max=12, message="El CI debe tener entre 6 y 12 digitos"),
        ],
        id="ci",
        render_kw={
            "placeholder": "CI: 99999",
            "autofocus": True,
        },
    )
    birthdate = DateField(
        "Fecha de nacimiento",
        validators=[
            InputRequired(),
            validate_adult,
        ],
    )
    submit = SubmitField("Ingresar")
