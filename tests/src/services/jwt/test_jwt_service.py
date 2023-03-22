from unittest.mock import patch
import pytest

from src.services.jwt.service import JwtTokenService
from .stubs import stub_user_model


@pytest.mark.asyncio
async def test_when_generate_token_then_returns_bearer_token_type():
    bearer_token = await JwtTokenService.generate_token(user_model=stub_user_model)

    assert bearer_token.get("token_type") == "bearer"


@pytest.mark.asyncio
async def test_when_generate_token_then_returns_access_token_string():
    bearer_token = await JwtTokenService.generate_token(user_model=stub_user_model)

    assert isinstance(bearer_token.get("access_token"), str)


@pytest.mark.asyncio
async def test_when_valid_jwt_then_return_true(jwt_token):
    is_valid = await JwtTokenService.validate_token(jwt=jwt_token)

    assert is_valid is True