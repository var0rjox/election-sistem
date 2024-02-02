from db.create_db import db, User, Voter, PoliticalParty, Vote, Candidate
from datetime import datetime, timedelta
from models.political_party import PoliticalParty as PoliticalPartyModel
from models.candidate import Candidate as CandidateModel
from models.vote import Vote as VoteModel


class DBService:
    def add_user(self, ci, name, birthdate, gender, password):
        new_user = User(
            ci=ci, name=name, birthdate=birthdate, gender=gender, password=password
        )
        db.session.add(new_user)
        db.session.commit()

    def get_user(self, ci):
        user = User.query.get(ci)
        return user

    def get_users(self):
        users = User.query.all()
        return users

    def add_voter(self, ci, name, birthdate, gender, is_enabled):
        new_voter = Voter(
            ci=ci, name=name, birthdate=birthdate, gender=gender, is_enabled=is_enabled
        )
        db.session.add(new_voter)
        db.session.commit()

    def get_voter(self, ci):
        voter = Voter.query.get(ci)
        return voter

    def update_voter_enabled(self, ci, enabled):
        voter = Voter.query.get(ci)
        voter.is_enabled = enabled
        db.session.commit()

    def get_voters(self):
        voters = Voter.query.all()
        return voters

    def get_political_parties(self):
        political_parties_db = (
            PoliticalParty.query.join(PoliticalParty.representative)
            .with_entities(
                PoliticalParty.id,
                PoliticalParty.name,
                PoliticalParty.acronym,
                PoliticalParty.description,
                PoliticalParty.logo,
                Candidate.ci,
                Candidate.name,
                Candidate.birthdate,
                Candidate.gender,
                Candidate.photo,
            )
            .all()
        )

        political_parties = []

        for party in political_parties_db:
            new_candidate = CandidateModel(
                ci=party[5],
                name=party[6],
                birthdate=party[7],
                gender=party[8],
                photo=party[9],
            )

            new_party = PoliticalPartyModel(
                name=party[1],
                acronym=party[2],
                description=party[3],
                logo=party[4],
                representative=new_candidate,
                id=party[0],
            )

            political_parties.append(new_party)

        return political_parties

    def add_political_party(self, name, acronym, description):
        new_party = PoliticalParty(name=name, acronym=acronym, description=description)
        db.session.add(new_party)
        db.session.commit()

    def get_political_party(self, id):
        party = PoliticalParty.query.get(id)
        return party

    def get_votes(self):
        votes_db = Vote.query.all()

        votes = []

        for vote in votes_db:
            party = self.get_political_party(vote.political_party_id)

            new_vote = VoteModel(
                elector_ci=vote.voter_id,
                candidate_voted=party.name,
                date_voted=vote.date_voted,
            )

            votes.append(new_vote)

        return votes

    def add_vote(self, voter_id, political_party_id):
        date_now = datetime.utcnow() + timedelta(hours=-4)
        new_vote = Vote(
            voter_id=voter_id,
            political_party_id=political_party_id,
            date_voted=date_now,
        )
        db.session.add(new_vote)
        db.session.commit()
