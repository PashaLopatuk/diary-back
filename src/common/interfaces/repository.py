from abc import ABC, abstractmethod


class BaseRepository[SessionType, ExpressionArgumentType](ABC):
    @abstractmethod
    async def create_one(self, model, async_session: SessionType):
        raise NotImplementedError

    @abstractmethod
    async def select_one(self, *clauses: ExpressionArgumentType, async_session: SessionType):
        raise NotImplementedError

