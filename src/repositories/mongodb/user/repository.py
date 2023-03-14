from typing import NoReturn

from decouple import config
from pymongo.results import UpdateResult

from src.domain.exceptions.services.exception import UserNotExists, UserAlreadyExists
from src.domain.models.user.model import NewUserModel, UserModel
from src.repositories.mongodb.base.base import MongoDbBaseRepository


class UserRepository(MongoDbBaseRepository):
    @classmethod
    async def _get_collection(cls):
        mongo_client = cls.infra.get_client()
        try:
            database = mongo_client[config("MONGODB_DATABASE_NAME")]
            collection = database[config("MONGODB_USER_COLLECTION")]

            return collection

        except Exception as ex:
            # logg
            raise ex

    @classmethod
    async def insert_one(cls, new_user: NewUserModel) -> NoReturn:
        collection = await cls._get_collection()
        user_template = new_user.get_user_template_to_save()

        try:
            result: UpdateResult = await collection.update_one(
                filter={"username": new_user.username}, update={"$setOnInsert": user_template}, upsert=True
            )

            if not result.upserted_id:
                raise UserAlreadyExists()

        except Exception as ex:
            # logg
            raise ex

    @classmethod
    async def find_one_by_username(cls, username: str) -> UserModel:
        collection = await cls._get_collection()

        try:
            user_data = await collection.find_one({"username": username})

            if not user_data:
                raise UserNotExists()

            return UserModel(user_data=user_data)

        except Exception as ex:
            # logg
            raise ex
