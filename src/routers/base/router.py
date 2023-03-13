from http import HTTPStatus

from fastapi import FastAPI, Request
from pydantic import ValidationError

from src.domain.enums.http_response.internal_code import InternalCode
from src.domain.models.http_response.model import ResponseModel
from src.routers.authentication.router import AuthenticationRouter
from src.routers.credit_card.router import CreditCardRouter
from src.routers.user.router import UserRouter


class BaseRouter:
    __app = FastAPI(title="Kubera API", description="Credit Card system")

    @classmethod
    def __include_credit_card_router(cls):
        credit_card_router = CreditCardRouter.get_credit_card_router()
        cls.__app.include_router(credit_card_router)
        return cls.__app

    @classmethod
    def __include_authentication_router(cls):
        auth_router = AuthenticationRouter.get_authentication_router()
        cls.__app.include_router(auth_router)
        return cls.__app

    @classmethod
    def __include_user_router(cls):
        user_router = UserRouter.get_user_router()
        cls.__app.include_router(user_router)
        return cls.__app

    @classmethod
    def register_routers(cls):
        cls.__include_credit_card_router()
        cls.__include_authentication_router()
        cls.__include_user_router()
        return cls.__app

    @staticmethod
    @__app.middleware("http")
    async def middleware_response(request: Request, call_next: callable):
        middleware_service_response = await BaseRouter.__process_request(
            request=request, call_next=call_next
        )
        return middleware_service_response

    @staticmethod
    async def __process_request(request: Request, call_next: callable):
        response = None

        try:
            response = await call_next(request)

        except ValidationError as ex:
            # logging here
            response = ResponseModel(
                success=False, internal_code=InternalCode.INVALID_PARAMS
            ).build_http_response(status_code=HTTPStatus.BAD_REQUEST)
            return response

        except Exception as ex:
            #  logging here
            response = ResponseModel(
                success=False, internal_code=InternalCode.INTERNAL_SERVER_ERROR
            ).build_http_response(status_code=HTTPStatus.INTERNAL_SERVER_ERROR)

        finally:
            return response
