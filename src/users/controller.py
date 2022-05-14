from fastapi import APIRouter, Depends
from .dto.create_user_dto import CreateUserDto
from .service import UsersService
from ..auth.service import get_current_user

router = APIRouter(
    tags = ['Users Controller'],
    prefix = '/users'
)

@router.get("/all")
def get_all_users(usersService: UsersService = Depends()):
    return usersService.getAll()
    

@router.get("/{user_id}")
def get_user(user_id: int, usersService: UsersService = Depends()):
    return usersService.get(user_id)


@router.post("/create")
def create_user(user: CreateUserDto, usersService: UsersService = Depends()):
    return usersService.createUser(user)

@router.delete("/delete/{user_id}")
def delete_user(user_id: int ,userService: UsersService = Depends()):
    return userService.deleteUser(user_id)
