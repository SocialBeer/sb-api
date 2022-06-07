from src.base.dto.base_dto import UserPasswordField, UserEmailField


class LoginDto(UserPasswordField, UserEmailField):
    pass