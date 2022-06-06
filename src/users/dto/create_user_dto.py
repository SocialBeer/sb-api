from pydantic import Field, Required

from .base_dto import BaseDto


class CreateUserDto(BaseDto):
    password: str = Field(
        default = Required, 
        min_length = 6, 
        example = "password",
        regex = "((?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{6,20})",
        description = "password should have at least one number, one lowercase and one uppercase"
    ) 