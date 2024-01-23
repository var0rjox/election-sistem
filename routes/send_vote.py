from flask import Blueprint, redirect, render_template, request, url_for, flash

send_vote = Blueprint('send_vote', __name__);

candidates = [
    # {'political_front_name': 'eew', 'president': 'Juanito', 'political_front': '21kl', 'img': 'https://yosoy.dev/wp-content/uploads/2012/08/hqdefault.jpg'},
    {'political_front_name': 'eew', 'president': 'Juanito', 'political_front': '21kl', 'img': 'https://www.tmladenov.dev/images/img-test.png', 'description': 'Descripcion para frente electoral'},
    {'political_front_name': 'loq', 'president': 'Maria', 'political_front': 'OHG', 'img': 'https://www.tmladenov.dev/images/img-test.png', 'description': 'Descripcion para frente electoral'},
    {'political_front_name': 'gdw', 'president': 'Leonardo', 'political_front': 'KLS', 'img': 'https://www.tmladenov.dev/images/img-test.png', 'description': 'Descripcion para frente electoral'},
    {'political_front_name': 'aae', 'president': 'Rosio', 'political_front': 'MJE', 'img': 'https://www.tmladenov.dev/images/img-test.png', 'description': 'Descripcion para frente electoral'},
]

@send_vote.route('/send_vote')
def vote():
    return render_template('send_vote.html', candidates = candidates)

@send_vote.route('/submit_vote', methods=['POST'])
def submit_vote():
    selected_candidate = request.form.get('selected_candidate')
    message = ''
    if selected_candidate == None:
        message = 'Seleccione un candidato'
        flash(message, 'alert')
    else:
        message = f'Candidato seleccionado: {selected_candidate}'
        flash(message, 'success')
    return redirect(url_for('send_vote.vote'))