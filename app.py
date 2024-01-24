from flask import Flask
from routes.home import home
from routes.user import user
from routes.committee import electoral_committee

app = Flask(__name__)

app.secret_key='mysecretkey'

app.register_blueprint(home)
app.register_blueprint(user)
app.register_blueprint(electoral_committee)

if __name__ == "__main__":
    #app.run()
    app.run(debug=True)