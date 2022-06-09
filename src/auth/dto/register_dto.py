from pydantic import BaseModel

from src.base.validation import user_validation


class RegisterDto(user_validation.BaseValidation):
    first_name: str
    last_name: str
    email: str
    country: str
    password: str