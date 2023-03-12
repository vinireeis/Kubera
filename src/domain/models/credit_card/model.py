from src.domain.validators.credit_card.validator import CreditCardValidator
from src.domain.models.expiration_date.model import ExpirationDateModel

from creditcard import CreditCard


class CreditCardModel:
    def __init__(self, payload: CreditCardValidator):
        self.number = payload.number  # tratar/ofuscar
        self.brand = self.get_brand(payload=payload)
        self.expiration_date = self.get_exp_date_formatted(payload=payload)
        self.holder = payload.holder
        self.cvv = payload.cvv

    @staticmethod
    def get_brand(payload: CreditCardValidator) -> str:
        number = payload.number
        credit_card = CreditCard(number=number)
        brand = credit_card.get_brand()
        return brand

    @staticmethod
    def get_exp_date_formatted(payload: CreditCardValidator):
        exp_date = payload.exp_date
        exp_date_formatted = ExpirationDateModel.format_to_save(exp_date=exp_date)

        return exp_date_formatted
