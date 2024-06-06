from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker, AsyncSession

from config import db_config


async def get_engine() -> AsyncEngine:
    engine = create_async_engine(
        url=db_config.url,
        echo=True,
        connect_args={"check_same_thread": False}
    )

    yield engine


async def create_async_session_maker(
    engine: Annotated[AsyncEngine, Depends(get_engine)]
) -> async_sessionmaker[AsyncSession]:
    async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)

    yield async_session_maker


async def create_async_session(
        session_maker: Annotated[async_sessionmaker[AsyncSession], Depends(create_async_session_maker)]
) -> AsyncSession:
    async with session_maker() as session:
        yield session
