from datetime import datetime
from typing import Union, Optional
import pytz

from creditcard import CreditCard
from dateparser import parse
from pydantic import BaseModel, validator, Extra, constr, ValidationError


class CreditCardValidator(BaseModel, extra=Extra.forbid):

    exp_date: str
    holder: constr(min_length=2)
    number: int
    cvv: Optional[int]

    @validator("cvv")
    def validate_cvv(cls, cvv) -> Union[int, None]:

        if not cvv:
            return cvv

        cvv_length = len(cvv)

        if 2 < cvv_length > 3:
            raise ValidationError("Cvv can only have between 2 and 3 numbers.")

        return cvv

    @validator("number")
    def validate_credit_card_number(cls, number) -> CreditCard:
        credit_card_instance = CreditCard(number=number)
        is_valid = credit_card_instance.is_valid()

        if not is_valid:
            raise ValidationError("Invalid credit card number")

        return credit_card_instance

    @validator("exp_date")
    def validate_exp_credit_card_date(cls, exp_date) -> datetime:
        try:
            expiration_date_converted = parse(exp_date)
        except Exception as ex:
            # logging
            raise ValidationError("Invalid expiration date format")

        today_datetime = datetime.today()
        credit_card_is_expired = expiration_date_converted > today_datetime

        if credit_card_is_expired:
            raise ValidationError("Expired credit card")

        return expiration_date_converted

exp_date = parse("/23/2023")
print(exp_date)
exp_date = exp_date.astimezone(tz=pytz.utc)
print(exp_date)

today = datetime.today()
print(today)
today = today.astimezone(tz=pytz.utc)
print(today)
is_expired = exp_date < today
# print(exp_date)
# print(exp_date.day)
print(is_expired)

