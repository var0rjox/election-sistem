from flask import session, render_template
from services.voters_service import VotersServices


voter_service = VotersServices()


def voter_load_information():
    ci = session["ci"]
    current_voter = voter_service.get_single_voter(ci)
    current_voter.type = 'voter'
    return render_template("voter-profile.html", person=current_voter)
