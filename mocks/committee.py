from models.user import User

users_committee = [
  User('12345678', 'esther'),
  User('87654321', 'gabriel'),
]

def get_user(ci):
  for user in users_committee:
    if user.ci == ci:
      return user
  return None