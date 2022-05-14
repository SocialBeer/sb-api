from .user_base_dto import UserBaseDto

class CreateUserDto(UserBaseDto):
    password: str

    