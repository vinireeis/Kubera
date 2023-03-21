from http import HTTPStatus

from src.domain.enums.http_response.internal_code import InternalCode
from src.domain.exceptions.base.exception import DomainException


class InvalidNumber(DomainException):
    def __init__(self, *args, **kwargs):
        self.msg = "The number must contain numeric characters only."
        self.status_code = HTTPStatus.BAD_REQUEST
        self.internal_code = InternalCode.DATA_VALIDATION_ERROR
        self.success = False
        super().__init__(
            self.msg,
            self.status_code,
            self.internal_code,
            self.success,
            *args,
            **kwargs
        )


class InvalidCreditCardNumber(DomainException):
    def __init__(self, *args, **kwargs):
        self.msg = "Invalid credit card number."
        self.status_code = HTTPStatus.BAD_REQUEST
        self.internal_code = InternalCode.DATA_VALIDATION_ERROR
        self.success = False
        super().__init__(
            self.msg,
            self.status_code,
            self.internal_code,
            self.success,
            *args,
            **kwargs
        )


class InvalidExpDate(DomainException):
    def __init__(self, *args, **kwargs):
        self.msg = 'Invalid expiry date format, use as follows "MM/YYYY" or "MM-YYYY".'
        self.status_code = HTTPStatus.BAD_REQUEST
        self.internal_code = InternalCode.DATA_VALIDATION_ERROR
        self.success = False
        super().__init__(
            self.msg,
            self.status_code,
            self.internal_code,
            self.success,
            *args,
            **kwargs
        )


class ExpiredCreditCard(DomainException):
    def __init__(self, *args, **kwargs):
        self.msg = "Credit card is expired"
        self.status_code = HTTPStatus.BAD_REQUEST
        self.internal_code = InternalCode.DATA_VALIDATION_ERROR
        self.success = False
        super().__init__(
            self.msg,
            self.status_code,
            self.internal_code,
            self.success,
            *args,
            **kwargs
        )


class InvalidCvv(DomainException):
    def __init__(self, *args, **kwargs):
        self.msg = "Cvv can only have between 2 and 3 numbers."
        self.status_code = HTTPStatus.BAD_REQUEST
        self.internal_code = InternalCode.DATA_VALIDATION_ERROR
        self.success = False
        super().__init__(
            self.msg,
            self.status_code,
            self.internal_code,
            self.success,
            *args,
            **kwargs
        )
