import pytest

from src.services.cryptography.service import CryptographyService
from tests.src.services.cryptography.stubs import stub_payload


@pytest.mark.asyncio
async def test_when_encrypt_number_then_return_expected_type():
    number_encrypted = await CryptographyService.encrypt_number(payload=stub_payload)

    assert isinstance(number_encrypted, bytes)


@pytest.mark.asyncio
async def test_when_decrypt_number_then_return_expected_type(stub_number):
    number_decrypted = await CryptographyService.decrypt_number(number=stub_number)
    assert isinstance(number_decrypted, str)


@pytest.mark.asyncio
async def test_when_decrypt_number_then_return_expected_values(stub_number):
    number_decrypted = await CryptographyService.decrypt_number(number=stub_number)
    assert number_decrypted == "5125975183938085"
