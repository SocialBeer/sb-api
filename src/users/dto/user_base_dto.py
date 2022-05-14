from pydantic import BaseModel


class UserBaseDto(BaseModel):
    username: str

    class Config:
        orm_mode = True

