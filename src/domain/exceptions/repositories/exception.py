from http import HTTPStatus

from src.domain.enums.http_response.internal_code import InternalCode
from src.domain.exceptions.base.exception import RepositoryException


class UserAlreadyExists(RepositoryException):
    def __init__(self, *args, **kwargs):
        self.msg = "User already exists, try again using other username"
        self.status_code = HTTPStatus.BAD_REQUEST
        self.internal_code = InternalCode.DATA_ALREADY_EXISTS
        self.success = False
        super().__init__(
            self.msg,
            self.status_code,
            self.internal_code,
            self.success,
            *args,
            **kwargs
        )


class UserNotExists(RepositoryException):
    def __init__(self, *args, **kwargs):
        self.msg = "User not exists"
        self.status_code = HTTPStatus.BAD_REQUEST
        self.internal_code = InternalCode.DATA_NOT_FOUND
        self.success = False
        super().__init__(
            self.msg,
            self.status_code,
            self.internal_code,
            self.success,
            *args,
            **kwargs
        )
