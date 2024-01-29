from models.vote import Vote
import datetime as dt


class VoteService:
    vote_list = []

    def add_vote(self, ci, candidate):
        vote = Vote(ci, candidate, dt.datetime.now())
        self.vote_list.append(vote)

    def get_all_votes(self):
        return self.vote_list
