from models.user import User

users_committee = [
  User('12345678', 'pequeñita'),
  User('87654321', 'pequeñito'),
]

def get_user(ci):
  for user in users_committee:
    if user.ci == ci:
      return user
  return None