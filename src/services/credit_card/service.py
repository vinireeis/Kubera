from src.domain.models.credit_card.model import CreditCardModel
from src.domain.validators.credit_card.validator import CreditCardValidator
from src.services.cryptography.service import CryptographyService


class CreditCardService:
    async def get_all_credit_cards(self):
        pass

    async def get_credit_card_details(self):
        pass

    async def register_new_credit_card(self, payload: CreditCardValidator):
        number_encrypted = await CryptographyService.encrypt_number(payload=payload)
        credit_card_model = CreditCardModel(
            payload=payload, number_encrypted=number_encrypted
        )
