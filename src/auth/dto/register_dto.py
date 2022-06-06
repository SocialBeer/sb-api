from pydantic import Field, Required

from .login_dto import LoginDto

class RegisterDto(LoginDto):
    first_name: str = Field(
        default = Required, 
        min_length = 3,
        max_length = 20,
        regex = "^[a-zA-Z]+$", 
        example = "Ivan"
    )
    last_name: str = Field(
        default = Required, 
        min_length = 3,
        max_length = 20,
        regex = "^[a-zA-Z]+$", 
        example = "Ivanov"
    )
    country: str = Field(
        default = Required, 
        min_length = 3,
        max_length = 20,
        regex = "^[a-zA-Z]+$", 
        example = "Poland"
    )