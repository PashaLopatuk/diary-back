from sqlalchemy.ext.asyncio import AsyncSession

from src.database.orm.models import User
from src.repositories.base import BaseOrmRepository


class UserRepository(BaseOrmRepository[User]):

    model = User

    async def create_user(self, user: dict, async_session: AsyncSession) -> User:
        return await self.create_one(instance=User(**user), async_session=async_session)

    async def select_user_by_id(self, selection_id: int, async_session: AsyncSession) -> User:
        exp = User.id == selection_id
        return await self.select_one(exp, async_session=async_session)

    async def select_user_by_username(self, username: str, async_session: AsyncSession) -> User:
        exp = User.username == username
        return await self.select_one(exp, async_session=async_session)
