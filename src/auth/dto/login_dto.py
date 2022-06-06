from pydantic import BaseModel, Field, Required


class LoginDto(BaseModel):
    email: str = Field(
        default = Required, 
        regex = "^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$", 
        example = "name@mail.com"
    )
    password: str = Field(
        default = Required, 
        min_length = 6, 
        example = "password",
        regex = "((?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{6,20})",
        description = "password should have at least one number, one lowercase and one uppercase"
    ) 