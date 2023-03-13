from src.domain.models.user.model import NewUserModel
from src.domain.validators.user.validator import UserValidator
from src.repositories.mongodb.user.repository import UserRepository


class UserService:
    @classmethod
    async def register_new_user(cls, payload: UserValidator) -> str:
        new_user_model = NewUserModel(payload=payload)
        await UserRepository.insert_one(new_user=new_user_model)

        return "user successfully registered"

