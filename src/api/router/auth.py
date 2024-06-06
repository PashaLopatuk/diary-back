from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.dependencies.sqlalchemy import create_async_session
from src.common.dto.queries.user import CreateUserQuery
from src.common.dto.responses.user import UserResponseModel

from src.database.orm.models.user import User
from src.handlers.auth.user import CreateUserHandler
from src.handlers.base import handler_factory

auth_router = APIRouter(prefix="/authentication", tags=["Authentication"])


@auth_router.post('/create_user/')
async def post_create_user(
    new_user: CreateUserQuery,
    async_session: Annotated[AsyncSession, Depends(create_async_session)]
):
    return await handler_factory(CreateUserHandler, async_session=async_session).handle(new_user)
