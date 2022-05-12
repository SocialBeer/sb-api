from pydantic import BaseModel

class UserDto(BaseModel):
    username: str

    class Config:
        orm_mode = True

