from flask import Flask
from routes.home import home
from routes.user import user

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(user)

if __name__ == "__main__":
    #app.run()
    app.run(debug=True)