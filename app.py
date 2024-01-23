from flask import Flask
from routes.home import home
from routes.user import user
from routes.elector import elector

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(user)
app.register_blueprint(elector)

if __name__ == "__main__":
    #app.run()
    app.run(debug=True)