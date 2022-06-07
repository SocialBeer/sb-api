from pydantic import Field, Required


password_field = Field(
    default = Required, 
    min_length = 6, 
    example = "password",
    regex = "((?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{6,20})",
    description = "password should have at least one number, one lowercase and one uppercase"
) 

email_field: str = Field(
    default = Required, 
    regex = "^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$", 
    example = "name@mail.com"
)

first_name_field: str = Field(
    default = Required, 
    min_length = 3,
    max_length = 20,
    regex = "^[a-zA-Z]+$", 
    example = "Ivan"
)

last_name_field: str = Field(
    default = Required, 
    min_length = 3,
    max_length = 20,
    regex = "^[a-zA-Z]+$", 
    example = "Ivanov"
)

country_field: str = Field(
    default = Required, 
    min_length = 3,
    max_length = 20,
    regex = "^[a-zA-Z]+$", 
    example = "Poland"
)