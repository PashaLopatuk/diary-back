from src.repositories.user import UserRepository
from src.services.user import UserService


class GatewayService:
    @staticmethod
    def user_service() -> UserService:
        return UserService(repository=UserRepository())
