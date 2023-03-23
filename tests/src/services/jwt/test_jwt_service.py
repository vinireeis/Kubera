import pytest
from jwt import ExpiredSignatureError, DecodeError

from src.services.jwt.service import JwtTokenService
from tests.src.services.jwt.stubs import stub_jwt_expired


@pytest.mark.asyncio
async def test_when_generate_token_then_returns_bearer_token_with_expected_values(stub_user):
    bearer_token = await JwtTokenService.generate_token(user_model=stub_user)

    assert bearer_token.get("access_token") is not None
    assert bearer_token.get("token_type") == "bearer"


@pytest.mark.asyncio
async def test_when_generate_token_then_returns_token_with_expected_types(stub_user):
    bearer_token = await JwtTokenService.generate_token(user_model=stub_user)

    assert isinstance(bearer_token, dict)
    assert isinstance(bearer_token.get("token_type"), str)
    assert isinstance(bearer_token.get("access_token"), str)


@pytest.mark.asyncio
async def test_when_valid_jwt_then_return_true(jwt_token):
    is_valid = await JwtTokenService.validate_token(jwt=jwt_token)

    assert is_valid is True


@pytest.mark.asyncio
async def test_when_invalid_jwt_then_raises():
    with pytest.raises(DecodeError):
        await JwtTokenService.validate_token(jwt="fake_jwt")


@pytest.mark.asyncio
async def test_when_expired_jwt_then_raises():
    with pytest.raises(ExpiredSignatureError):
        await JwtTokenService.validate_token(jwt=stub_jwt_expired)


@pytest.mark.asyncio
async def test_when_decode_token_then_returns_expected_types(jwt_token):
    token_decoded = await JwtTokenService.decode_token(jwt=jwt_token)

    assert isinstance(token_decoded, dict)
    assert isinstance(token_decoded.get("username"), str)
    assert isinstance(token_decoded.get("id"), str)
    assert isinstance(token_decoded.get("exp"), int)
