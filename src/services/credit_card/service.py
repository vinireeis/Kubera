from typing import List

from src.domain.exceptions.services.exception import CreditCardAlreadyRegistered, CreditCardNotExists
from src.domain.models.credit_card.model import NewCreditCardModel, UserCreditCardsModel
from src.domain.validators.credit_card.validator import CreditCardValidator
from src.repositories.mongodb.credit_card.repository import CreditCardRepository
from src.services.cryptography.service import CryptographyService
from src.services.jwt.service import JwtTokenService


class CreditCardService:
    @classmethod
    async def get_all_credit_cards(cls, token: str) -> dict:
        decrypted_token = await JwtTokenService.decode_token(jwt=token)
        numbers_decrypted = await cls.__get_all_credit_card_decrypted(
            decrypted_token=decrypted_token
        )

        return {"credit_card": numbers_decrypted}

    @classmethod
    async def get_credit_card_details(cls, number: str, token: str):
        decrypted_token = await JwtTokenService.decode_token(jwt=token)
        credit_cards_result = await CreditCardRepository.find_all_credit_cards(
            decrypted_token=decrypted_token
        )
        credit_cards_data = credit_cards_result[0].get("credit_card")

        if not credit_cards_data:
            raise CreditCardNotExists()

        credit_cards_model = UserCreditCardsModel(credit_cards_data=credit_cards_data)
        credit_card_details_template = (
            await credit_cards_model.get_credit_card_details_template(number=number)
        )

        return credit_card_details_template

    @classmethod
    async def register_new_credit_card(
        cls, payload: CreditCardValidator, token: str
    ) -> str:
        decrypted_token = await JwtTokenService.decode_token(jwt=token)
        numbers_decrypted = await cls.__get_all_credit_card_decrypted(
            decrypted_token=decrypted_token
        )
        await cls.__validate_credit_card_already_exists(
            numbers_decrypted=numbers_decrypted, payload=payload
        )
        number_encrypted = await CryptographyService.encrypt_number(payload=payload)

        credit_card_model = NewCreditCardModel(
            payload=payload,
            number_encrypted=number_encrypted,
            decrypted_token=decrypted_token,
        )

        await CreditCardRepository.insert_one_credit_card(credit_card=credit_card_model)

        return "Credit card registered successfully"

    @staticmethod
    async def __get_all_credit_card_decrypted(decrypted_token: dict) -> List:
        credit_cards_data = await CreditCardRepository.find_all_credit_card_numbers(
            decrypted_token=decrypted_token
        )
        numbers = credit_cards_data[0].get("credit_card")

        if not numbers:
            return []

        numbers_decrypted = [
            await CryptographyService.decrypt_number(number_decrypted.get("number"))
            for number_decrypted in numbers
        ]

        return numbers_decrypted

    @staticmethod
    async def __validate_credit_card_already_exists(
        numbers_decrypted: List, payload: CreditCardValidator
    ) -> bool:
        if payload.number in numbers_decrypted:
            raise CreditCardAlreadyRegistered()

        return True
