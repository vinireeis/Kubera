from datetime import datetime
from typing import Union, Optional

import pytz
from creditcard import CreditCard
from dateparser import parse
from pydantic import BaseModel, validator, Extra, constr, ValidationError


class CreditCardValidator(BaseModel, extra=Extra.forbid):
    exp_date: Union[str, datetime]
    holder: constr(min_length=2)
    number: constr(min_length=13, max_length=19)
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
    def validate_credit_card_number_is_numeric(cls, number) -> str:
        if not number.is_numeric():
            raise ValidationError("The number must contain numeric characters only.")

        return number

    @validator("number")
    def validate_credit_card_number(cls, number) -> str:
        credit_card = CreditCard(number=number)
        is_valid = credit_card.is_valid()

        if not is_valid:
            raise ValidationError("Invalid credit card number.")

        return number

    @validator("exp_date")
    def validate_exp_credit_card_date(cls, exp_date) -> datetime:
        try:
            expiration_date_converted = parse(exp_date)
            expiration_date_utc = expiration_date_converted.astimezone(tz=pytz.utc)
        except Exception as ex:
            # logging
            raise ValidationError(
                'invalid expiry date format, use as follows "MM/YYYY" or "MM-YYYY".'
            )

        today_datetime = datetime.today()
        today_utc = today_datetime.astimezone(tz=pytz.utc)
        credit_card_is_expired = expiration_date_utc > today_utc

        if credit_card_is_expired:
            raise ValidationError("Expired credit card.")

        return expiration_date_utc
