from pydantic import BaseModel,Field, Required


class UserPasswordField(BaseModel):
    password: str = Field(
        default = Required, 
        min_length = 6, 
        example = "password",
        regex = "((?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{6,20})",
        description = "password should have at least one number, one lowercase and one uppercase"
    ) 


class UserEmailField(BaseModel):
    email: str = Field(
        default = Required, 
        regex = "^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$", 
        example = "name@mail.com"
    )


class UserInformationFields(BaseModel):
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