from datetime import datetime
from re import sub
from typing import Union, Optional

import loglifos
from creditcard import CreditCard
from dateparser import parse
from pydantic import BaseModel, validator, Extra, constr
from pytz import utc

from src.domain.exceptions.domain.exception import (
    InvalidNumber,
    InvalidCreditCardNumber,
    InvalidExpDate,
    ExpiredCreditCard,
    InvalidCvv,
)


class CreditCardValidator(BaseModel, extra=Extra.forbid):
    exp_date: str
    holder: constr(min_length=2)
    number: constr(min_length=13, max_length=19)
    cvv: Optional[int]

    @validator("cvv")
    def validate_cvv(cls, cvv) -> Union[int, None]:
        if not cvv:
            return cvv

        cvv_length = len(str(cvv))

        if 2 < cvv_length > 3:
            raise InvalidCvv()

        return int(cvv)

    @validator("number")
    def remove_simbols_and_empty_characters(cls, number):
        number = sub("[!@#$%&*() ]", "", number)
        return number

    @validator("number")
    def validate_credit_card_number_is_numeric(cls, number) -> str:
        try:
            int(number)

        except Exception as ex:
            loglifos.error(exception=ex, msg=str(ex))
            raise InvalidNumber()

        return number

    @validator("number")
    def validate_credit_card_number(cls, number) -> str:
        try:
            credit_card = CreditCard(number=number)
            is_valid = credit_card.is_valid()

            if not is_valid:
                raise InvalidCreditCardNumber()

        except Exception as ex:
            loglifos.error(exception=ex, msg=str(ex))
            raise InvalidCreditCardNumber()

        return number

    @validator("exp_date")
    def validate_exp_credit_card_date(cls, exp_date) -> datetime:
        try:
            expiration_date_converted = parse(exp_date)
            expiration_date_utc = expiration_date_converted.astimezone(tz=utc)

        except Exception as ex:
            loglifos.error(exception=ex, msg=str(ex))
            raise InvalidExpDate()

        today_datetime = datetime.today()
        today_utc = today_datetime.astimezone(tz=utc)
        credit_card_is_expired = expiration_date_utc < today_utc

        if credit_card_is_expired:
            raise ExpiredCreditCard()

        return expiration_date_utc
