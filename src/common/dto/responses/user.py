from src.common.dto.base import BasePydanticModel


class UserResponseModel(BasePydanticModel):
    id: int
    username: str