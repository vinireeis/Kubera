from typing import NoReturn

import loglifos
from fastapi.security import OAuth2PasswordRequestForm
from passlib.hash import bcrypt

from src.domain.exceptions.services.exception import (
    InvalidPassword,
    InvalidOrExpiredToken,
)
from src.domain.models.user.model import UserModel
from src.repositories.mongodb.user.repository import UserRepository
from src.services.jwt.service import JwtTokenService


class AuthenticationService:
    @staticmethod
    async def generate_token(form: OAuth2PasswordRequestForm) -> dict:
        user_model = await UserRepository.find_one_by_username(username=form.username)
        await AuthenticationService.verify_password_hash(
            form=form, user_model=user_model
        )

        token = await JwtTokenService.generate_token(user_model=user_model)
        return token

    @staticmethod
    async def verify_token(token) -> NoReturn:
        try:
            await JwtTokenService.validate_token(jwt=token)

        except Exception as ex:
            loglifos.error(exception=ex, msg=str(ex))
            raise InvalidOrExpiredToken()

    @staticmethod
    async def verify_password_hash(
        form: OAuth2PasswordRequestForm, user_model: UserModel
    ) -> bool:
        secret = form.password
        password_is_valid = bcrypt.verify(secret=secret, hash=user_model.password_hash)

        if not password_is_valid:
            raise InvalidPassword()

        return True
