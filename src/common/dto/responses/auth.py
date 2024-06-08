from src.common.dto.base import BasePydanticModel


class LoginResponseModel(BasePydanticModel):
    message: str
    token: str
