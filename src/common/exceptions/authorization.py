from src.common.exceptions.base import BaseException


class AuthenticationException(BaseException):
    status_code = 401

    title = "Authentication Error"

    def __init__(self, message=None):
        self.message = message

