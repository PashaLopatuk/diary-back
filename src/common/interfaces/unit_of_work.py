

from sqlalchemy.ext.asyncio import AsyncSession


class UnitOfWork:
    def __init__(self, async_session: AsyncSession) -> None:
        self.__async_session = async_session

    async def __aenter__(self) -> AsyncSession:

        return self.__async_session

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is None:
            await self.__async_session.commit()
        else:
            await self.__async_session.rollback()

        await self.__async_session.close()
