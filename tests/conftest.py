import pytest_asyncio

from tests.src.services.jwt.stubs import stub_user_data
from src.domain.models.user.model import UserModel
from src.services.jwt.service import JwtTokenService


@pytest_asyncio.fixture(scope="function")
async def stub_user():
    stub_user_model = UserModel(user_data=stub_user_data)
    return stub_user_model


@pytest_asyncio.fixture(scope="function")
async def jwt_token(stub_user) -> str:
    token_bearer = await JwtTokenService.generate_token(user_model=stub_user)
    jwt = token_bearer.get("access_token")
    return jwt


@pytest_asyncio.fixture(scope="function")
async def stub_number():
    stub_number = eval("b'gAAAAABkG7D7EOlrFIMPzwACMHTjKaQ9Bfr-ce2x_ScpuzFDItEnBLgHSxxB4lbDs2QjqE_XaCoVGl_5Gyjs7Y9Ypc_ktc1mLSHwpAQywR22cRKeDEVHua8='")
    return stub_number
