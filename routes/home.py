from flask import Blueprint, request, session, render_template, redirect, url_for, flash

# from time import strptime

from forms.voter_login import VoterLogin

# from utils.is_legal_age import is_legal_age

home = Blueprint("home", __name__)


@home.route("/", methods=["GET", "POST"])
def login():
    if "ci" in session:
        return redirect(url_for("home.voter_profile"))

    form = VoterLogin()
    is_form_valid = form.validate_on_submit()

    if not is_form_valid:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"{error}", "danger")

        return render_template("voter-login.html", form=form)

    if is_form_valid:
        ci = form.ci.data
        user = True

        if user:
            # TODO: If already voted then redirect to login
            if False:
                flash(
                    "Usted no esta habilitado para votar, debido a que ya ejerció su derecho al voto",
                    "danger",
                )
                return redirect(url_for("home.login"))

            session["ci"] = ci
            return redirect(url_for("home.voter_profile"))

        else:
            flash(
                "El número de cédula no está registrado en el padrón electoral",
                "danger",
            )
            return redirect(url_for("home.login"))

    return render_template("voter-login.html", form=form)


@home.route("/perfil-votante")
def voter_profile():
    if "ci" not in session:
        flash("Debe iniciar sesión para poder votar", "danger")
        return redirect(url_for("home.login"))
    else:
        ci = session["ci"]
        return render_template("voter-profile.html", ci=ci)


@home.route("/voter-logout")
def voter_logout():
    session.pop("ci", None)
    return redirect(url_for("home.login"))
