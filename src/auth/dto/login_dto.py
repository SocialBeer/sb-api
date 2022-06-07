from pydantic import BaseModel

from src.base.validation import user_validation 


class LoginDto(BaseModel):
    email: str
    password: str