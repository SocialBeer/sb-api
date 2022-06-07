from src.base.dto.base_dto import UserEmailField, UserInformationFields, UserPasswordField


class CreateUserDto(UserEmailField, UserInformationFields, UserPasswordField):
    pass