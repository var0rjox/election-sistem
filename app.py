from flask import Flask
from routes.home import home
from routes.user import user
from routes.send_vote import send_vote

app = Flask(__name__)

app.secret_key='mysecretkey'

app.register_blueprint(home)
app.register_blueprint(user)
app.register_blueprint(send_vote)

if __name__ == "__main__":
    #app.run()
    app.run(debug=True)