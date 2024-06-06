from src.common.dto.queries.user import CreateUserQuery
from src.common.dto.responses.user import UserResponseModel
from src.handlers.base import BaseHandler
from src.services.user import UserService


class CreateUserHandler(BaseHandler[CreateUserQuery, UserResponseModel]):
    async def handle(self, query: CreateUserQuery) -> UserResponseModel:
        user_service = self.service_gateway.user_service()

        async with self.unit_of_work as session:
            return await user_service.post_user(instance=query, async_session=session)

