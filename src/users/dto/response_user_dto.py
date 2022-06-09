from pydantic import BaseModel


class ResponseUserDto(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    country: str