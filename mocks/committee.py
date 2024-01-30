from datetime import date
from models.user import User

users_committee = [
    User(
        name="Esther",
        birthdate=date(2002, 1, 17),
        ci="12345678",
        gender="F",
        password="esther",
        photo="https://fzdzxwhgvlbyvouhhsxy.supabase.co/storage/v1/object/public/photos/esther.JPG",
    ),
]
