from pydantic import BaseModel
from src.base.validation import user_validation


class CreateUserDto(BaseModel):
    first_name: str = user_validation.first_name_field
    last_name: str = user_validation.last_name_field
    email: str = user_validation.email_field
    password: str = user_validation.password_field
    country: str = user_validation.country_field