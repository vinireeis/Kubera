from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt

from src.domain.exceptions.services.exception import InvalidPassword
from src.repositories.mongodb.user.repository import UserRepository


class AuthenticationService:
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    @staticmethod
    async def authenticate_user(form: OAuth2PasswordRequestForm):
        await AuthenticationService.verify_password_hash(form=form)
        pass

    @staticmethod
    async def verify_password_hash(form: OAuth2PasswordRequestForm):
        username = form.username
        user = await UserRepository.find_one_by_username(username=username)
        secret = form.password
        password_is_valid = bcrypt.verify(secret=secret, hash=user.password_hash)

        if not password_is_valid:
            raise InvalidPassword()

        return True
