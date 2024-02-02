from services.db_service import DBService

db_service = DBService()


class CommitteeService:
    def get_users(self):
        users = db_service.get_users()
        return users

    def get_user(self, ci):
        user = db_service.get_user(ci)
        return user
