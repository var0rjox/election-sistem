from flask import Blueprint, request, session, render_template, redirect, url_for, flash
from time import strptime

from utils.is_legal_age import is_legal_age

home = Blueprint('home', __name__)

@home.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        ci = request.form['ci']
        birthdate = request.form['birthdate']
        birthdate_formated = strptime(birthdate, "%Y-%m-%d")

        if not ci.isdigit() or len(ci) < 6:
            flash("El número de cédula debe ser un número de al menos 6 dígitos", "danger")
            return redirect(url_for('home.login'))

        # If birtdate is not valid (at least 18 years old) then redirect to login
        if is_legal_age(birthdate_formated) == False:
            flash("Debe ser mayor de edad para poder votar", "danger")
            return redirect(url_for('home.login'))

        # TODO: If is not in db then redirect to login
        if False:
            flash("El número de cédula no está registrado en el padrón electoral", "danger")
            return redirect(url_for('home.login'))

        # TODO: If already voted then redirect to login
        if False:
            flash("Usted no esta habilitado para votar, debido a que ya ejerció su derecho al voto", "danger")
            return redirect(url_for('home.login'))

        session['ci'] = ci
        return redirect(url_for('home.voter_profile'))
    else:
        if 'ci' in session:
            return redirect(url_for('home.voter_profile'))
        else:
            return render_template('voter-login.html')


@home.route('/voter-profile')
def voter_profile():
    if 'ci' not in session:
        flash("Debe iniciar sesión para poder votar", "danger")
        return redirect(url_for('home.login'))
    else:
        ci = session['ci']
        return render_template('voter-profile.html', ci=ci)


@home.route('/voter-logout')
def voter_logout():
    session.pop('ci', None)
    return redirect(url_for('home.login'))