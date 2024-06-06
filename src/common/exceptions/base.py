class BaseException(Exception):
    title: str
    description: str

    status_code: int


class BaseApplicationException(Exception):
    status_code = 500

    def __init__(self, message: str, details: dict | None = None) -> None:
        self.message: str = message
        self.details = details if details is not None else None
