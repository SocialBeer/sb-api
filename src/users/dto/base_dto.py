from pydantic import BaseModel, Required, Field


class BaseDto(BaseModel):
    email: str = Field(
        default = Required, 
        regex = "^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$", 
        example = "name@mail.com"
    )
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