from flask import Flask
from routes.home import home
from routes.user import user
from routes.electoral_committee.committee import electoral_committee

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(user)
app.register_blueprint(electoral_committee)

if __name__ == "__main__":
    #app.run()
    app.run(debug=True, host='192.168.0.7', port=9323)