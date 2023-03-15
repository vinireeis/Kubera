from http import HTTPStatus

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from src.domain.enums.http_response.internal_code import InternalCode
from src.domain.models.http_response.model import ResponseModel
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
    async def get_all_credit_cards(token: str = Depends(oauth2_scheme)):
        await AuthenticationService.verify_token(token=token)
        result = await CreditCardService.get_all_credit_cards(token=token)
        response = ResponseModel(
            result=result, internal_code=InternalCode.SUCCESS, success=True
        ).build_http_response(status_code=HTTPStatus.OK)

        return response

    @staticmethod
    @__router.get("/credit-card/{number}")
    async def get_credit_card_details(number: str, token: str = Depends(oauth2_scheme)):
        await AuthenticationService.verify_token(token=token)
        result = await CreditCardService.get_credit_card_details(number=number, token=token)
        response = ResponseModel(
            result=result, internal_code=InternalCode.SUCCESS, success=True
        ).build_http_response(status_code=HTTPStatus.OK)

        return response

    @staticmethod
    @__router.post("/credit-card")
    async def register_new_credit_card(
        payload: CreditCardValidator, token: str = Depends(oauth2_scheme)
    ):
        await AuthenticationService.verify_token(token=token)
        message = await CreditCardService.register_new_credit_card(
            payload=payload, token=token
        )
        response = ResponseModel(
            message=message, internal_code=InternalCode.SUCCESS, success=True
        ).build_http_response(status_code=HTTPStatus.OK)

        return response
