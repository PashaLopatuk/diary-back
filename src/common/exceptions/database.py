from src.common.exceptions.base import BaseException


class AlreadyExistsException(BaseException):
    status_code = 409

    def __init__(self, message, details=None):
        self.message = message
        self.details = details
