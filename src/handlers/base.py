from logging import Handler
from typing import TypeVar, Type
from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from src.common.interfaces.unit_of_work import UnitOfWork
from src.services.gateway import GatewayService


class AbstractHandler(ABC):
    @abstractmethod
    async def handle[Query, Response](self, query: Query) -> Response:
        raise NotImplementedError


class BaseHandler[Query, Response](AbstractHandler):

    def __init__(
            self,
            async_session: AsyncSession,
    ):
        self.service_gateway = GatewayService()
        self.unit_of_work = UnitOfWork(async_session=async_session)

    @abstractmethod
    async def handle(self, query: Query) -> Response:
        raise NotImplementedError


HandlerType = TypeVar("HandlerType", bound=BaseHandler)


def handler_factory(
        handler: Type[HandlerType],
        async_session: AsyncSession,
) -> HandlerType:
    return handler(async_session)
