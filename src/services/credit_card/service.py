from src.domain.exceptions.services.exception import CreditCardAlreadyRegistered
from src.domain.models.credit_card.model import CreditCardModel
from src.domain.validators.credit_card.validator import CreditCardValidator
from src.repositories.mongodb.credit_card.repository import CreditCardRepository
from src.services.cryptography.service import CryptographyService
from src.services.jwt.service import JwtTokenService


class CreditCardService:
    async def get_all_credit_cards(self):
        pass

    async def get_credit_card_details(self):
        pass

    @classmethod
    async def register_new_credit_card(cls, payload: CreditCardValidator, token: str):
        decrypted_token = await JwtTokenService.decode_token(jwt=token)
        await cls.validate_credit_card_already_exists(payload=payload, decrypted_token=decrypted_token)
        number_encrypted = await CryptographyService.encrypt_number(payload=payload)
        credit_card_model = CreditCardModel(
            payload=payload,
            number_encrypted=number_encrypted,
            decrypted_token=decrypted_token,
        )
        await CreditCardRepository.insert_one_credit_card(credit_card=credit_card_model)

        return "Credit card registered successfully"

    @staticmethod
    async def validate_credit_card_already_exists(payload: CreditCardValidator, decrypted_token: dict):
        credit_cards_data = await CreditCardRepository.find_all_credit_cards(decrypted_token=decrypted_token)
        numbers = credit_cards_data[0].get("credit_card")

        numbers_decrypted = [await CryptographyService.decrypt_number(number_decrypted.get("number")) for number_decrypted in numbers]
        if payload.number in numbers_decrypted:
            raise CreditCardAlreadyRegistered()

        return True



