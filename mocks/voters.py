from datetime import date
from models.voter import Voter


voters = [
    Voter(
        ci="1234567",
        birthdate=date(2002, 5, 5),
        is_enabled=True,
        name="Juan Perez",
        gender="Male",
        photo="https://picsum.photos/200/300",
    ),
    Voter(
        ci="7654321",
        birthdate=date(1990, 1, 1),
        is_enabled=True,
        name="Maria Perez",
        gender="Female",
        photo="https://picsum.photos/200/300",
    ),
    Voter(
        ci="123456",
        birthdate=date(2000, 4, 4),
        is_enabled=True,
        name="Juan Perez",
        gender="Male",
        photo="https://picsum.photos/200/300",
    ),
]
