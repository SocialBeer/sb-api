from .login_dto import LoginDto
from src.base.dto.base_dto import UserInformationFields, UserEmailField

class RegisterDto(LoginDto, UserInformationFields, UserEmailField):
    pass