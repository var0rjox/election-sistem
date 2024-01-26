from flask import Flask
from routes.home import home
from routes.user import user
from routes.voter import voter
from routes.vote import vote

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(user)
app.register_blueprint(voter)
app.register_blueprint(vote)

if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
