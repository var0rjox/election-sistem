from flask import Blueprint, request


vote = Blueprint("vote", __name__, url_prefix="/enviar-voto")


@vote.route("/", methods=["GET", "POST"])
def index():
    return (
        "Voto procesado"
        if request.method == "POST"
        else "Esta es la seccion para votar"
    )
