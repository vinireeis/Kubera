from enum import IntEnum


class InternalCode(IntEnum):
    SUCCESS = 0
    INVALID_PARAMS = 10
    INVALID_AUTHENTICATION = 30
    UNAUTHORIZED = 40
    DATA_VALIDATION_ERROR = 50
