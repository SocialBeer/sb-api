from fastapi import Depends, HTTPException, status, security

from src.users.dto.user_base_dto import UserBaseDto
from ..database import get_session
from sqlalchemy.orm import Session
from .dto.create_user_dto import CreateUserDto
from .dto.user_dto import UserDto
from .model import UserModel
from ..config import config
from ..auth.service import AuthService


class UsersService:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
    
    def get(self, id: int) -> UserDto:
        user = self.session.query(UserModel).filter_by(id = id).first()
        if not user:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
        return UserDto(id = user.id, username = user.username)

    def createUser(self, createUserDto: CreateUserDto) -> CreateUserDto: 
        user = UserModel(
            username = createUserDto.username, 
            password_hash = AuthService.generatePasswordHash(createUserDto.password)
        )
        try:
            self.session.add(user) 
            self.session.commit()
        except:
            self.session.rollback()
            
        return CreateUserDto(username = user.username, password = user.password_hash)
    
    def deleteUser(self, id: int) -> UserBaseDto:
        user = self.session.query(UserModel).filter_by(id = id).first()

        if not user:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
        
        try:
            self.session.delete(user)
            self.session.commit()
        except:
            self.session.rollback()

        return UserBaseDto(
            username = user.username
        )

    def getAll(self):
        return self.session.query(UserModel).all()



