from src.repositories.auth import AuthRepository
from src.services.auth import AuthService


class GatewayService:
    @staticmethod
    def user_service() -> AuthService:
        return AuthService(repository=AuthRepository())
    