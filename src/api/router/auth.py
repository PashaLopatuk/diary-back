from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.dependencies.sqlalchemy import create_async_session

from src.common.dto.queries.auth import LoginCredentialsModel
from src.common.dto.queries.user import CreateUserQuery
from src.common.dto.responses.user import UserResponseModel
from src.common.exceptions.authorization import AuthenticationException
from src.common.exceptions.base import BaseApplicationException
from src.common.exceptions.database import AlreadyExistsException

from src.handlers.auth.auth import CreateUserHandler, GetUserHandler, LoginUserHandler
from src.handlers.base import handler_factory


auth_router = APIRouter(prefix="/authentication", tags=["Authentication"])


@auth_router.post('/register/')
async def post_create_user(
        new_user: CreateUserQuery,
        async_session: Annotated[AsyncSession, Depends(create_async_session)]
) -> UserResponseModel:
    try:
        return await handler_factory(CreateUserHandler, async_session=async_session).handle(new_user)
    except AlreadyExistsException as error:
        raise HTTPException(status_code=error.status_code, detail=error.message)
    except BaseApplicationException as error:
        raise HTTPException(status_code=error.status_code, detail=error.message)


@auth_router.get('/get_user/{user_id}')
async def get_read_user(
        user_id: int,
        async_session: Annotated[AsyncSession, Depends(create_async_session)]
) -> UserResponseModel:
    try:
        return await handler_factory(GetUserHandler, async_session=async_session).handle(user_id)
    except BaseApplicationException as error:
        raise HTTPException(status_code=error.status_code, detail=error.message)


@auth_router.post('/login/')
async def post_login(
        credentials: LoginCredentialsModel,
        async_session: Annotated[AsyncSession, Depends(create_async_session)]
):
    try:
        return await handler_factory(handler=LoginUserHandler, async_session=async_session).handle(credentials)
    except BaseApplicationException as error:
        raise HTTPException(status_code=error.status_code, detail=error.message)
    except AuthenticationException as error:
        raise HTTPException(status_code=error.status_code, detail=error.message)

