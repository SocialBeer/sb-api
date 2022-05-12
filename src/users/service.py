from fastapi import Depends
from ..database import get_session
from sqlalchemy.orm import Session
from .dto.create_user_dto import CreateUserDto
from .model import UserModel


class UsersService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
    
    def createUser(self, userDto: CreateUserDto) -> UserModel: #Домашнее задание разобраться как сделать функцию асинхронной
        user = UserModel(**userDto.dict())
        print(user.id)
        try:
            self.session.add(user) 
            self.session.commit()
        except:
            self.session.rollback()
            
        return user
    
    def getAll(self):
        return self.session.query(UserModel).all()



