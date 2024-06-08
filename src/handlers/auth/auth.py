from src.common.dto.queries.auth import LoginCredentialsModel
from src.common.dto.queries.user import CreateUserQuery
from src.common.dto.responses.auth import LoginResponseModel
from src.common.dto.responses.user import UserResponseModel
from src.handlers.base import BaseHandler


class CreateUserHandler(BaseHandler[CreateUserQuery, UserResponseModel]):
    async def handle(self, query: CreateUserQuery) -> UserResponseModel:
        user_service = self.service_gateway.user_service()

        async with self.unit_of_work as session:
            return await user_service.post_user(instance=query, async_session=session)


class GetUserHandler(BaseHandler[UserResponseModel, UserResponseModel]):
    async def handle(self, user_id: int) -> UserResponseModel:
        user_service = self.service_gateway.user_service()

        async with self.unit_of_work as session:
            return await user_service.get_user(
                selection_id=user_id,
                username=None,
                async_session=session
            )

class LoginUserHandler(BaseHandler[UserResponseModel, UserResponseModel]):
    async def handle(self, credentials: LoginCredentialsModel) -> LoginResponseModel:
        user_service = self.service_gateway.user_service()

        async with self.unit_of_work as session:
            return await user_service.login_user(
                credentials=credentials,
                async_session=session
            )
