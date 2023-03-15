from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.services.authentication.service import AuthenticationService


class AuthenticationRouter:
    __router = APIRouter(prefix="/api/v1", tags=["User authentication"])

    @classmethod
    def get_authentication_router(cls):
        return cls.__router

    @staticmethod
    @__router.post("/token")
    async def get_token(form: OAuth2PasswordRequestForm = Depends()) -> dict:
        response = await AuthenticationService.generate_token(form=form)
        return response
