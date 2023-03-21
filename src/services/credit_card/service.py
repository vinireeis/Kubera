from src.domain.exceptions.services.exception import (
    CreditCardAlreadyRegistered,
    CreditCardNotExists,
)
from src.domain.models.credit_card.model import NewCreditCardModel, UserCreditCardsModel
from src.domain.validators.credit_card.validator import CreditCardValidator
from src.repositories.mongodb.credit_card.repository import CreditCardRepository
from src.services.cryptography.service import CryptographyService
from src.services.jwt.service import JwtTokenService


class CreditCardService:
    @classmethod
    async def get_all_credit_cards(cls, token: str) -> dict:
        decrypted_token = await JwtTokenService.decode_token(jwt=token)
        user_credit_cards = await cls.__get_all_credit_cards_decrypted(
            decrypted_token=decrypted_token
        )

        credit_cards_template = user_credit_cards.get_credit_cards_template()

        return credit_cards_template

    @classmethod
    async def get_credit_card_details(cls, number: str, token: str):
        decrypted_token = await JwtTokenService.decode_token(jwt=token)
        user_credit_cards = await cls.__get_all_credit_cards_decrypted(
            decrypted_token=decrypted_token
        )

        credit_card_details_template = (
            user_credit_cards.get_credit_card_details_template(number=number)
        )

        if not credit_card_details_template:
            raise CreditCardNotExists()

        return credit_card_details_template

    @classmethod
    async def register_new_credit_card(
        cls, payload: CreditCardValidator, token: str
    ) -> str:
        decrypted_token = await JwtTokenService.decode_token(jwt=token)
        user_credit_cards = await cls.__get_all_credit_cards_decrypted(
            decrypted_token=decrypted_token
        )
        await cls.__validate_credit_card_already_exists(
            user_credit_cards=user_credit_cards, payload=payload
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
    async def __get_all_credit_cards_decrypted(
        decrypted_token: dict,
    ) -> UserCreditCardsModel:
        credit_cards_result = await CreditCardRepository.find_all_credit_cards(
            decrypted_token=decrypted_token
        )
        credit_cards_data = credit_cards_result[0].get("credit_card")

        if not credit_cards_data:
            credit_cards_data = []

        for credit_card in credit_cards_data:
            number = credit_card.get("number")
            decrypted_number = await CryptographyService.decrypt_number(number=number)
            credit_card.update(number=decrypted_number)

        user_credit_cards = UserCreditCardsModel(
            credit_cards_decrypted=credit_cards_data
        )

        return user_credit_cards

    @staticmethod
    async def __validate_credit_card_already_exists(
        user_credit_cards: UserCreditCardsModel, payload: CreditCardValidator
    ) -> bool:
        if payload.number in user_credit_cards.credit_cards:
            raise CreditCardAlreadyRegistered()

        return True
