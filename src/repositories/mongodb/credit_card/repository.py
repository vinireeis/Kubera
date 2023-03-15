from typing import List

import loglifos
from decouple import config

from src.domain.models.credit_card.model import CreditCardModel
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
    async def insert_one_credit_card(cls, credit_card: CreditCardModel):
        collection = await cls._get_collection()
        credit_card_template = credit_card.get_template_to_save()

        try:
            await collection.update_one(
                filter={"id": credit_card.user_id},
                update={"$push": {"credit_card": credit_card_template}},
            )

        except Exception as ex:
            loglifos.error(exception=ex, msg=str(ex))
            raise ex

    @classmethod
    async def find_one_credit_card_details(cls, credit_card: CreditCardModel):
        collection = await cls._get_collection()

        try:
            result = await collection.find_one(
                {"id": credit_card.user_id, "credit_card.number": credit_card.number_encrypted}
            )
            return result

        except Exception as ex:
            loglifos.error(exception=ex, msg=str(ex))
            raise ex

    @classmethod
    async def find_all_credit_cards(cls, decrypted_token) -> List:
        collection = await cls._get_collection()
        id = decrypted_token.get("id")

        try:
            cursor = collection.find({"id": id}, {"credit_card.number": 1, "_id": 0})
            credit_cards_data = [credit_card for credit_card in await cursor.to_list(length=100)]
            return credit_cards_data

        except Exception as ex:
            loglifos.error(exception=ex, msg=str(ex))
            raise ex
