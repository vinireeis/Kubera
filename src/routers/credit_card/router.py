from fastapi import APIRouter, Request, Depends
from fastapi.security import OAuth2PasswordBearer

from src.domain.validators.credit_card.validator import CreditCardValidator
from src.services.authentication.service import AuthenticationService
from src.services.credit_card.service import CreditCardService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/token")


class CreditCardRouter:
    __router = APIRouter(prefix="/api/v1", tags=["Credit Card"])

    @staticmethod
    def get_credit_card_router():
        return CreditCardRouter.__router

    @staticmethod
    @__router.get("/credit-card")
    async def get_all_credit_cards(request: Request, token: str = Depends(oauth2_scheme)):
        pass

    @staticmethod
    @__router.get("/credit-card/{number}")
    async def get_credit_card_details(request: Request, number: int, token: str = Depends(oauth2_scheme)):
        pass

    @staticmethod
    @__router.post("/credit-card")
    async def register_new_credit_card(payload: CreditCardValidator, token: str = Depends(oauth2_scheme)):
        await AuthenticationService.verify_token(token=token)
        message = await CreditCardService.register_new_credit_card(payload=payload)
