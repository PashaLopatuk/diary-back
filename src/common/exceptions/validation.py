class ValidationError(BaseException):
    status_code = 422
    def __init__(self, message, details=None):
        self.message = message
        self.details = details

