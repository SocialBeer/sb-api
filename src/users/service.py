from fastapi import Depends, HTTPException, status
from werkzeug.security import generate_password_hash
from sqlalchemy.orm import Session
from typing import List

from .dto.response_user_dto import ResponseUserDto
from ..database import get_session
from .dto.create_user_dto import CreateUserDto
from .model import UserModel



class UsersService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
    
    def _findUser(self, id: int) -> UserModel:
        user = self.session.query(UserModel).filter_by(id = id).first()

        if not user:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)

        return user

    def getUser(self, id: int) -> ResponseUserDto:
        user = self._findUser(id)
        
        return ResponseUserDto(id = user.id, username = user.username)

    def createUser(self, createUserDto: CreateUserDto) -> ResponseUserDto: 
        user = UserModel(
            username = createUserDto.username, 
            password_hash = generate_password_hash(createUserDto.password)
        )

        try:
            self.session.add(user) 
            self.session.commit()
        except:
            self.session.rollback()
            
        return ResponseUserDto(id = user.id, username = user.username)
    
    def deleteUser(self, id: int) -> ResponseUserDto:
        user = self._findUser(id)
        
        try:
            self.session.delete(user)
            self.session.commit()
        except:
            self.session.rollback()

        return ResponseUserDto(id = user.id, username = user.username)

    def getAll(self) -> List[ResponseUserDto]:
        return self.session.query(UserModel).all()