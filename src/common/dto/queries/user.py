from src.common.dto.base import BasePydanticModel


class CreateUserQuery(BasePydanticModel):
    username: str
    password: str
