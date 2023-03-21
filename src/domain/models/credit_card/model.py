from re import sub
from typing import List, NoReturn

from creditcard import CreditCard

from src.domain.exceptions.domain.exception import InvalidNumber
from src.domain.models.expiration_date.model import ExpirationDateModel
from src.domain.validators.credit_card.validator import CreditCardValidator


class NewCreditCardModel:
    def __init__(
        self,
        payload: CreditCardValidator,
        number_encrypted: bytes,
        decrypted_token: dict,
    ):
        self.brand = self.get_brand(payload=payload)
        self.cvv = payload.cvv
        self.expiration_date = self.get_exp_date_formatted(payload=payload)
        self.holder = payload.holder
        self.number_encrypted = number_encrypted
        self.user_id = decrypted_token.get("id")

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
    def get_exp_date_formatted(payload: CreditCardValidator) -> str:
        exp_date = payload.exp_date
        exp_date_formatted = ExpirationDateModel.format_to_save(exp_date=exp_date)

        return exp_date_formatted

    @staticmethod
    def get_brand(payload: CreditCardValidator) -> str:
        number = payload.number
        credit_card = CreditCard(number=number)
        brand = credit_card.get_brand()

        return brand


class UserCreditCardsModel:
    def __init__(self, credit_cards_decrypted: List):
        self.credit_cards = [
            CreditCardModel(credit_card_data=credit_card)
            for credit_card in credit_cards_decrypted
        ]

    def get_credit_card_details_template(self, number: str):
        template = {}
        number_treated = self.__regex_number(number=number)
        self.__is_numeric(number=number_treated)
        for credit_card in self.credit_cards:
            if number_treated == credit_card.number:
                template = credit_card.get_credit_card_template(number=number_treated)

        return template

    def get_credit_cards_template(self) -> dict:
        template = {
            "credit_cards": [credit_card.number for credit_card in self.credit_cards]
        }

        return template

    @staticmethod
    def __regex_number(number: str) -> str:
        number = sub("[!@#$%&*() ]", "", number)
        return number

    @staticmethod
    def __is_numeric(number: str) -> NoReturn:
        if not number.isnumeric():
            raise InvalidNumber()


class CreditCardModel:
    def __init__(self, credit_card_data: dict):
        self.number = credit_card_data.get("number")
        self.cvv = credit_card_data.get("cvv")
        self.holder = credit_card_data.get("holder")
        self.exp_date = self.get_exp_date_formatted(credit_card_data=credit_card_data)

    def get_credit_card_template(self, number: str) -> dict:
        template = {
            "credit_card": {
                "number": number,
                "cvv": self.cvv,
                "holder": self.holder,
                "exp_date": self.exp_date,
            }
        }

        return template

    @staticmethod
    def get_exp_date_formatted(credit_card_data: dict) -> str:
        exp_date = credit_card_data.get("exp_date")
        exp_date_formatted = ExpirationDateModel.format_to_show(exp_date=exp_date)

        return exp_date_formatted
