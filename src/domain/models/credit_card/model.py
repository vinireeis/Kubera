from creditcard import CreditCard

from src.domain.models.expiration_date.model import ExpirationDateModel
from src.domain.validators.credit_card.validator import CreditCardValidator


class CreditCardModel:
    def __init__(self, payload: CreditCardValidator, number_encrypted: bytes):
        self.number_encrypted = number_encrypted
        self.brand = self.get_brand(payload=payload)
        self.expiration_date = self.get_exp_date_formatted(payload=payload)
        self.holder = payload.holder
        self.cvv = payload.cvv

    def get_template_to_save(self) -> dict:
        template = {
            "exp_date": self.expiration_date,
            "holder": self.holder,
            "number": self.number_encrypted,
        }

        if self.cvv:
            template.update(cvv=self.cvv)

        return template

    @staticmethod
    def get_brand(payload: CreditCardValidator) -> str:
        number = payload.number
        credit_card = CreditCard(number=number)
        brand = credit_card.get_brand()

        return brand

    @staticmethod
    def get_exp_date_formatted(payload: CreditCardValidator) -> str:
        exp_date = payload.exp_date
        exp_date_formatted = ExpirationDateModel.format_to_save(exp_date=exp_date)

        return exp_date_formatted
