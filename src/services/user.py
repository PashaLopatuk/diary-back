from sqlalchemy.ext.asyncio import AsyncSession

from src.common.dto.queries.user import CreateUserQuery
from src.common.dto.responses.user import UserResponseModel
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

        new = instance.model_dump(exclude={'password'})
        new['hashed_password'] = instance.password

        user = await self.repository.create_user(new, async_session=async_session)

        return UserResponseModel.model_validate(user)