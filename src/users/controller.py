from fastapi import APIRouter, Depends
from typing import List

from .dto.response_user_dto import ResponseUserDto
from .dto.create_user_dto import CreateUserDto
from .service import UsersService


router = APIRouter(
    tags = ['Users Controller'],
    prefix = '/users'
)

@router.get("/all")
def get_all_users(usersService: UsersService = Depends()) -> List[ResponseUserDto]:
    return usersService.getAll()
    
@router.get("/{user_id}", response_model = ResponseUserDto)
def get_user(user_id: int, usersService: UsersService = Depends()) -> ResponseUserDto:
    return usersService.getUser(user_id)

@router.post("/create")
def create_user(user: CreateUserDto, usersService: UsersService = Depends()) -> ResponseUserDto:
    return usersService.createUser(user)

@router.delete("/delete/{user_id}")
def delete_user(user_id: int, userService: UsersService = Depends()) -> ResponseUserDto:
    return userService.deleteUser(user_id)
