from .login_dto import LoginDto

class RegisterDto(LoginDto):
    first_name: str
    last_name: str
    country: str 