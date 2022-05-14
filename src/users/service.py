from fastapi import Depends, HTTPException, status
from src.users.dto.user_base_dto import UserBaseDto
from ..database import get_session
from sqlalchemy.orm import Session
from .dto.create_user_dto import CreateUserDto
from .model import UserModel
from typing import List
from werkzeug.security import generate_password_hash


class UsersService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
    
    def getUser(self, id: int) -> UserModel:
        user = self.session.query(UserModel).filter_by(id = id).first()
        if not user:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
        return user

    def createUser(self, createUserDto: CreateUserDto) -> CreateUserDto: 
        user = UserModel(
            username = createUserDto.username, 
            password_hash = generate_password_hash(createUserDto.password)
        )
        try:
            self.session.add(user) 
            self.session.commit()
        except:
            self.session.rollback()
            
        return CreateUserDto(username = user.username, password = user.password_hash)
    
    def deleteUser(self, id: int) -> UserBaseDto:
        user = self.getUser(id)
        
        try:
            self.session.delete(user)
            self.session.commit()
        except:
            self.session.rollback()

        return UserBaseDto(
            username = user.username
        )

    def getAll(self) -> List[UserModel]:
        return self.session.query(UserModel).all()