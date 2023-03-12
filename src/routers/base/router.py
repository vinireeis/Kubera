from fastapi import FastAPI, Request

from src.routers.credit_card.router import CreditCardRouter


class BaseRouter:
    __app = FastAPI(title="Kubera API", description="Credit Card system")

    @classmethod
    def __include_credit_card_router(cls):
        credit_card_router = CreditCardRouter.get_credit_card_router()
        cls.__app.include_router(credit_card_router)
        return cls.__app

    @classmethod
    def register_routers(cls):
        cls.__include_credit_card_router()
        return cls.__app

    @staticmethod
    @__app.middleware("http")
    async def middleware_response(request: Request, call_next: callable):
        middleware_service_response = await BaseRouter.__add_process_time_header(
            request=request, call_next=call_next
        )
        return middleware_service_response

    @staticmethod
    async def __add_process_time_header(request: Request, call_next: callable):
        response = None

        try:
            response = await call_next(request)

        except Exception as ex:
            pass
            #  logging here
            # response = "pass"

        finally:
            return response
