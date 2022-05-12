from .user_dto import UserDto

class CreateUserDto(UserDto):
    password_hash: str

    