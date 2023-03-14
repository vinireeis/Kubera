from uuid import uuid4

from passlib.hash import bcrypt

from src.domain.validators.user.validator import UserValidator


class NewUserModel:
    def __init__(self, payload: UserValidator):
        self.username = payload.username
        self.password = payload.password
        self.password_hash = bcrypt.hash(secret=payload.password)
        self.id = str(uuid4())

    def get_user_template_to_save(self) -> dict:
        template = {
            "username": self.username,
            "password": self.password_hash,
            "id": self.id,
        }

        return template


class UserModel:
    def __init__(self, user_data: dict):
        self.id = user_data.get("id")
        self.username = user_data.get("username")
        self.password_hash = user_data.get("password")
        self.credit_cards = user_data.get("credit_card")
