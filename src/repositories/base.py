from typing import Any

from sqlalchemy import ColumnExpressionArgument, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.common.interfaces.repository import BaseRepository
from src.database.orm.base import Base


class BaseOrmRepository(BaseRepository[AsyncSession, ColumnExpressionArgument]):

    model: Any

    async def select_one(self, *clauses: ColumnExpressionArgument, async_session: AsyncSession):
        stmt = select(self.model).where(*clauses)
        result = await async_session.execute(stmt)

        return result.scalars().first()

    async def create_one(self, instance, async_session: AsyncSession):
        async_session.add(instance)
        await async_session.commit()
        await async_session.refresh(instance)

        await async_session.close()

        return instance

