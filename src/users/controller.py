from fastapi import APIRouter, Depends
from .dto.user_base_dto import UserBaseDto
from .dto.user_dto import UserDto
from .dto.create_user_dto import CreateUserDto
from .service import UsersService
from typing import List


router = APIRouter(
    tags = ['Users Controller'],
    prefix = '/users'
)

@router.get("/all")
def get_all_users(usersService: UsersService = Depends()) -> List[UserDto]:
    return usersService.getAll()
    
@router.get("/{user_id}", response_model = UserDto)
def get_user(user_id: int, usersService: UsersService = Depends()) -> UserDto:
    return usersService.getUser(user_id)

@router.post("/create")
def create_user(user: CreateUserDto, usersService: UsersService = Depends()) -> CreateUserDto:
    return usersService.createUser(user)

@router.delete("/delete/{user_id}")
def delete_user(user_id: int ,userService: UsersService = Depends()) -> UserBaseDto:
    return userService.deleteUser(user_id)
