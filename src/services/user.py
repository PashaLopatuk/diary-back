from sqlalchemy.ext.asyncio import AsyncSession

from src.common.dto.queries.user import CreateUserQuery
from src.common.dto.responses.user import UserResponseModel
from src.common.exceptions.database import AlreadyExistsException
from src.common.utils.security.verify import get_password_hash
from src.repositories.user import UserRepository
from src.services.base import BaseService


class UserService(BaseService[UserRepository]):
    async def get_user(
            self, selection_id: int | None, username: str | None, async_session: AsyncSession
    ) -> UserResponseModel:
        if selection_id is not None:
            user = await self.repository.select_user_by_id(selection_id=selection_id, async_session=async_session)
        else:
            user = await self.repository.select_user_by_username(username=username, async_session=async_session)

        return UserResponseModel.model_validate(user)

    async def post_user(
            self, instance: CreateUserQuery, async_session: AsyncSession
    ) -> UserResponseModel:

        existing_user = await self.repository.select_user_by_username(instance.username, async_session)
        if existing_user:
            raise AlreadyExistsException(f"User with username '{instance.username}' already exists")

        user_payload = instance.model_dump(exclude={'password'})
        hashed_password = get_password_hash(instance.password)
        user_payload['hashed_password'] = hashed_password

        user = await self.repository.create_user(user_payload, async_session=async_session)

        return UserResponseModel.model_validate(user)
