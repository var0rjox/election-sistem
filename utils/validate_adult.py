from flask_wtf import FlaskForm
from wtforms import DateField, ValidationError
from datetime import date


def validate_adult(form: FlaskForm, field: DateField):
    today = date.today()
    age = (
        today.year
        - field.data.year
        - ((today.month, today.day) < (field.data.month, field.data.day))
    )
    if age < 18:
        raise ValidationError("Debe ser mayor de edad para poder votar")
