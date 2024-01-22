from flask import Flask
from routes.home import home
from routes.user import user
from routes.election_results import election_results

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(user)
app.register_blueprint(election_results)

if __name__ == "__main__":
    #app.run()
    app.run(debug=True)