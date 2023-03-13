from decouple import config

from src.domain.models.credit_card.model import CreditCardModel
from src.domain.validators.credit_card.validator import CreditCardValidator
from src.repositories.mongodb.base.base import MongoDbBaseRepository


class CreditCardRepository(MongoDbBaseRepository):
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
    async def insert_one_credit_card(cls, credit_card_model: CreditCardModel):
        collection = await cls._get_collection()
        credit_card_template = credit_card_model.get_template_to_save()

        try:
            await collection.insert_one(credit_card_template)

        except Exception as ex:
            # logg
            raise ex

    @classmethod
    async def find_one_by_credit_card_number(cls, payload: CreditCardValidator):
        collection = await cls._get_collection()
        number = payload.number

        try:
            result = await collection.find_one({"number": number})
            return result

        except Exception as ex:
            # logg
            raise ex

    @classmethod
    async def find_all_credit_cards(cls):
        collection = await cls._get_collection()

        try:
            result = await collection.find()
            return result

        except Exception as ex:
            # logg
            raise ex
