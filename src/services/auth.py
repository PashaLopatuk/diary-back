from sqlalchemy.ext.asyncio import AsyncSession

from src.common.dto.queries.auth import LoginCredentialsModel
from src.common.dto.queries.user import CreateUserQuery
from src.common.dto.responses.user import UserResponseModel
from src.common.exceptions.authorization import AuthenticationException
from src.common.exceptions.database import AlreadyExistsException, NoRecordsFoundException
from src.common.utils.security.verify import get_password_hash, verify_password
from src.repositories.auth import AuthRepository
from src.services.base import BaseService


class AuthService(BaseService[AuthRepository]):
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

    async def login_user(
            self,
            credentials: LoginCredentialsModel,
            async_session: AsyncSession
    ):
        existing_user = await self.repository.select_user_by_username(
            username=credentials.username,
            async_session=async_session
        )

        if not existing_user:
            raise NoRecordsFoundException(message=f"User with username '{credentials.username}' does not exists")

        user = await self.repository.select_user_by_username(
            username=credentials.username,
            async_session=async_session
        )

        hashed_password = user.hashed_password

        plain_password = credentials.password

        if verify_password(plain_password, hashed_password):
            return UserResponseModel.model_validate(user)
        else:
            raise AuthenticationException("Incorrect password")
