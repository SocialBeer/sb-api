from src.base.dto.base_dto import UserEmailField, UserInformationFields


class ResponseUserDto(UserEmailField, UserInformationFields):
    id: int