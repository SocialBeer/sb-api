import pydantic


from pydantic import BaseModel


class ResponseUserDto(BaseModel):
    id: int
    username: str