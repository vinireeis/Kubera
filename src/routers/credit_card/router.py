from fastapi import APIRouter, Request, Response, Depends

from src.domain.validators.credit_card.validator import CreditCardValidator


class CreditCardRouter:
    __router = APIRouter(prefix="/api/v1", tags=["Credit Card"])

    @staticmethod
    def get_credit_card_router():
        return CreditCardRouter.__router

    @staticmethod
    @__router.get("/credit-card")
    async def get_all_credit_cards(request: Request):
        pass

    @staticmethod
    @__router.get("/credit-card/{number}")
    async def get_credit_card_details(request: Request, number: int):
        pass

    @staticmethod
    @__router.post("/credit-card")
    async def register_new_credit_card(
        request: Request, payload: CreditCardValidator = Depends()
    ):
        pass
