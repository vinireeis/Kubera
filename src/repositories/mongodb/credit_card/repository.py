from decouple import config

from src.domain.models.credit_card.model import CreditCardModel
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
    async def register_credit_card(
        cls, credit_card: CreditCardModel
    ):
        collection = await cls._get_collection()
        credit_card_template = CreditCardModel.get_template_to_save()
        try:
            await collection.insert_one(credit_card_template)
        except Exception as ex:
            # logg
            raise ex
