from pydantic import BaseModel


class CreateUserDto(BaseModel):
    username: str
    password: str

    