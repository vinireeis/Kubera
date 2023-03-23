from src.domain.validators.credit_card.validator import CreditCardValidator


credit_card_data = {
      "exp_date": "12/2027",
      "holder": "Vinicius",
      "number": "5125 9751 8393 8085",
      "cvv": 956
    }

stub_payload = CreditCardValidator(**credit_card_data)
