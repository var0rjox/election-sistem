from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


db = SQLAlchemy()


class Voter(db.Model):
    ci = db.Column(db.String(12), primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    is_enabled = db.Column(db.Boolean, nullable=False)
    photo = db.Column(db.Text, default="")
    vote = db.relationship("Vote", backref="voter")

    def __repr__(self):
        return "<Name %r>" % self.name


class User(db.Model):
    ci = db.Column(db.String(12), primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    photo = db.Column(db.Text, default="")
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return "<Name %r>" % self.name


class Candidate(db.Model):
    ci = db.Column(db.String(12), primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    birthdate = db.Column(db.Date, nullable=True)
    gender = db.Column(db.String(1), nullable=False)
    photo = db.Column(db.Text, default="")
    political_party_id = db.Column(db.Integer, db.ForeignKey("political_party.id"))

    def __repr__(self):
        return "<Name %r>" % self.name


class PoliticalParty(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=True)
    acronym = db.Column(db.String(10), nullable=True)
    description = db.Column(db.Text, nullable=True)
    logo = db.Column(db.Text, default="")
    representative = db.relationship("Candidate", backref="political_party")
    vote = db.relationship("Vote", backref="political_party")

    def __repr__(self):
        return "<Name %r>" % self.name


class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    voter_id = db.Column(db.String(12), db.ForeignKey("voter.ci"), primary_key=True)
    political_party_id = db.Column(
        db.Integer, db.ForeignKey("political_party.id"), primary_key=True
    )
    date_voted = db.Column(db.DateTime(timezone=True))


def create_db(app):
    global db
    with app.app_context():
        db.drop_all()
        db.create_all()

        with app.open_resource("./db/script.sql", mode="r") as archivo_sql:
            for linea in archivo_sql:
                if linea != "\n":
                    db.session.execute(text(linea))
        db.session.commit()
