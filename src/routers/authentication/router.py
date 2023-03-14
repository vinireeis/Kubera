from http import HTTPStatus

from fastapi import APIRouter, Response, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.domain.enums.http_response.internal_code import InternalCode
from src.domain.models.http_response.model import ResponseModel
from src.services.authentication.service import AuthenticationService


class AuthenticationRouter:
    __router = APIRouter(prefix="/api/v1", tags=["User authentication"])

    @staticmethod
    def get_authentication_router():
        return AuthenticationRouter.__router

    @staticmethod
    @__router.post("/token")
    async def get_token(form: OAuth2PasswordRequestForm = Depends()) -> Response:
        result = await AuthenticationService.generate_token(form=form)
        response = ResponseModel(
            success=True, result=result, internal_code=InternalCode.SUCCESS
        ).build_http_response(status_code=HTTPStatus.OK)

        return response
