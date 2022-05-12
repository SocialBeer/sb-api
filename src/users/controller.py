from fastapi import APIRouter, Depends
from .dto.create_user_dto import CreateUserDto
from .service import UsersService


router = APIRouter(
    tags = ['Users Controller'],
    prefix = '/users'
)

@router.get("/all")
def get_all_users(usersService: UsersService = Depends()):
    return usersService.getAll()
    

@router.post("/create")
def create_user(user: CreateUserDto, usersService: UsersService = Depends()):
    return usersService.createUser(user)
