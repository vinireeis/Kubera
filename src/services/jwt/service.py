from datetime import datetime, timedelta

import jwt as jwt_lib
from decouple import config
from pytz import timezone

from src.domain.models.user.model import UserModel


class JwtTokenService:
    key = config("JWT_SECRET_KEY")
    algorithm = config("JWT_ALGORITHM")

    @classmethod
    async def generate_token(cls, user_model: UserModel) -> dict:
        payload = await cls.__get_jwt_payload(user_model=user_model)
        jwt_token = jwt_lib.encode(
            payload=payload, key=cls.key, algorithm=cls.algorithm
        )
        bearer_token = {"access_token": jwt_token, "token_type": "bearer"}

        return bearer_token

    @classmethod
    async def validate_token(cls, jwt: str):
        jwt_lib.decode(
            jwt=jwt, key=cls.key, algorithms=cls.algorithm, do_time_check=True
        )

        return True

    @classmethod
    async def decode_token(cls, jwt: str):
        token_decoded = jwt_lib.decode(jwt=jwt, key=cls.key, algorithms=cls.algorithm)

        return token_decoded

    @staticmethod
    async def __get_jwt_payload(user_model: UserModel) -> dict:
        jwt_data = dict()
        jwt_data.update({"username": user_model.username})
        jwt_data.update({"id": user_model.id})
        jwt_data.update(
            {
                "exp": datetime.now(timezone("America/Sao_Paulo"))
                + timedelta(seconds=int(config("JWT_TTL"))),
            }
        )

        return jwt_data
