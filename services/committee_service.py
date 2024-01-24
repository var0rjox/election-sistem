from mocks.committee import users_committee


class CommitteeService:
    def get_users(self):
        return users_committee

    def get_user(self, ci):
        for user in users_committee:
            if user.ci == ci:
                return user
        return None
