from flask import Blueprint, redirect, render_template, url_for

# import time

send_vote = Blueprint("send_vote", __name__)

candidates = [
    {
        "political_front_name": "eew",
        "president": "Juanito",
        "political_front": "21kl",
        "img": "https://www.tmladenov.dev/images/img-test.png",
        "description": "Descripcion para frente electoral",
    },
    {
        "political_front_name": "loq",
        "president": "Maria",
        "political_front": "OHG",
        "img": "https://www.tmladenov.dev/images/img-test.png",
        "description": "Descripcion para frente electoral",
    },
    {
        "political_front_name": "gdw",
        "president": "Leonardo",
        "political_front": "KLS",
        "img": "https://www.tmladenov.dev/images/img-test.png",
        "description": "Descripcion para frente electoral",
    },
    {
        "political_front_name": "aae",
        "president": "Rosio",
        "political_front": "MJE",
        "img": "https://www.tmladenov.dev/images/img-test.png",
        "description": "Descripcion para frente electoral",
    },
]


@send_vote.route("/send_vote")
def vote():
    return render_template("send_vote.html", candidates=candidates)


@send_vote.route("/submit_vote", methods=["POST"])
def submit_vote():
    # for i in range(2, 0, -1):
    #     time.sleep(1)
    return redirect(url_for("home.voter_logout"))
