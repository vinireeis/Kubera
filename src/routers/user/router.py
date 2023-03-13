from http import HTTPStatus

from fastapi import APIRouter, Response

from src.domain.enums.http_response.internal_code import InternalCode
from src.domain.models.http_response.model import ResponseModel
from src.domain.validators.user.validator import UserValidator
from src.services.user.service import UserService


class UserRouter:
    __router = APIRouter(prefix="/api/v1", tags=["User registration"])

    @staticmethod
    def get_user_router():
        return UserRouter.__router

    @staticmethod
    @__router.post("/user")
    async def create_user(payload: UserValidator) -> Response:
        message = await UserService.register_new_user(payload=payload)
        response = ResponseModel(
            success=True, message=message, internal_code=InternalCode.SUCCESS
        ).build_http_response(status_code=HTTPStatus.CREATED)
        return response
