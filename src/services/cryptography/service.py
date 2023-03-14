from cryptography.fernet import Fernet
from decouple import config

from src.domain.models.credit_card.model import CreditCardModel
from src.domain.validators.credit_card.validator import CreditCardValidator


class CryptographyService:
    fernet_crypter = Fernet(config("KUBERA_ENCRYPTION_KEY").encode())

    @classmethod
    async def encrypt_number(cls, payload: CreditCardValidator) -> bytes:
        data = payload.number.encode()
        number_encrypted = cls.fernet_crypter.encrypt(data=data)

        return number_encrypted

    @classmethod
    async def decrypt_number(cls, payload: CreditCardModel) -> str:
        token = payload.number_encoded  # TODO: ajustar com o obj de retorno do banco
        decrypted_number = cls.fernet_crypter.decrypt(token=token)
        number = decrypted_number.decode()
        return number
