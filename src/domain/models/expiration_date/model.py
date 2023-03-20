from datetime import datetime

from dateparser import parse
from dateutil.relativedelta import relativedelta


class ExpirationDateModel:
    @staticmethod
    def format_to_save(exp_date: datetime) -> str:
        exp_date_with_last_day_of_month = exp_date + relativedelta(day=31)
        exp_date_formatted = exp_date_with_last_day_of_month.strftime("%Y-%m-%d")

        return exp_date_formatted

    @staticmethod
    def format_to_show(exp_date: str) -> str:
        exp_date_to_datetime = parse(exp_date)
        exp_date_formatted = exp_date_to_datetime.strftime("%m/%Y")
        return exp_date_formatted
