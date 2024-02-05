from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import InputRequired, Length


class Login(FlaskForm):
    ci = PasswordField(
        "Carnet de identidad",
        validators=[InputRequired(), Length(min=7, max=10)],
        id="ci-committee",
        render_kw={
            "placeholder": "CI: 99999",
            "autofocus": True,
        },
    )
    password = PasswordField(
        "Contraseña",
        validators=[InputRequired(), Length(min=6, max=12)],
        id="password-committee",
    )
    submit = SubmitField("Ingresar")
