from src.common.dto.base import BasePydanticModel


class LoginCredentialsModel(BasePydanticModel):
    username: str
    password: str
