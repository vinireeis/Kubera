from http import HTTPStatus

from fastapi import APIRouter, Response
from fastapi.security import OAuth2PasswordRequestForm

from src.services.authentication.service import AuthenticationService
from src.services.user.service import UserService
from src.domain.enums.http_response.internal_code import InternalCode
from src.domain.models.http_response.model import ResponseModel


class AuthenticationRouter:
    __router = APIRouter(prefix="/api/v1", tags=["User authentication"])

    @staticmethod
    def get_authentication_router():
        return AuthenticationRouter.__router

    @staticmethod
    @__router.get("/token")
    async def get_token(form: OAuth2PasswordRequestForm) -> Response:
        result = AuthenticationService.authenticate_user(form=form)
        response = ResponseModel(
            success=True, result=result, internal_code=InternalCode.SUCCESS
        ).build_http_response(status_code=HTTPStatus.OK)

        return response
