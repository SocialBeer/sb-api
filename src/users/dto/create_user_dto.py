from pydantic import BaseModel


class CreateUserDto(BaseModel):
    email: str
    first_name: str
    last_name: str
    country: str
    password: str

    