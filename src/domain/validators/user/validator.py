from pydantic import BaseModel, constr


class UserValidator(BaseModel):
    username: str
    password: constr(min_length=6, max_length=15)
