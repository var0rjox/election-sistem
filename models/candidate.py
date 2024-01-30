from datetime import date
from .voter import Voter
from .candidate_position import CandidatePosition


class Candidate(Voter):
    def __init__(
        self,
        ci,
        name,
        birthdate: date,
        gender,
        photo,
        is_enabled=True,
        position: CandidatePosition = None,
    ):
        super().__init__(ci, name, birthdate, gender, photo, is_enabled)
        self.__position = position

    @property
    def position(self):
        return self.__position
