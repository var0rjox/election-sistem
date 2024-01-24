from flask import Blueprint, render_template, redirect, url_for, flash, session
from forms.committee_login import Login
from services.committee_service import CommitteeService

electoral_committee = Blueprint(
    "electoral_committee",
    __name__,
    url_prefix="/comite-electoral",
    template_folder="../../templates",
)
committee_service = CommitteeService()


@electoral_committee.route("/login", methods=["GET", "POST"])
def login():
    form = Login()
    if form.validate_on_submit():
        ci = form.ci.data
        password = form.password.data

        # Verificar en la db
        user = committee_service.get_user(ci)

        if user:
            if user.password == password:
                session["ci"] = user.ci
                return redirect(url_for("electoral_committee.profile"))
            else:
                flash("Credenciales incorrectas.", "danger")
                return redirect(url_for("electoral_committee.login"))
        else:
            flash("El usuario no esta registrado.", "danger")
            return redirect(url_for("electoral_committee.login"))

    if "ci" in session:
        return redirect(url_for("electoral_committee.profile"))

    return render_template("committee_login.html", form=form)


@electoral_committee.route("/perfil")
def profile():
    if "ci" not in session:
        return redirect(url_for("electoral_committee.login"))
    return render_template("committee_profile.html")


@electoral_committee.route("/logout")
def logout():
    session.pop("ci", None)
    return redirect(url_for("electoral_committee.login"))
