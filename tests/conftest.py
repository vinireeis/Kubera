import pytest


from tests.src.services.jwt.stubs import stub_user_model
from src.services.jwt.service import JwtTokenService


@pytest.fixture(scope="function")
async def jwt_token() -> str:
    token_bearer = await JwtTokenService.generate_token(user_model=stub_user_model)
    jwt = token_bearer.get("access_token")
    return jwt
