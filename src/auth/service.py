from fastapi import Depends, security, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_session
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import jwt
from .dto.auth_dto import AuthDto
from ..config import config
from ..users.model import UserModel


oauth2_scheme = security.OAuth2PasswordBearer(tokenUrl="/users/auth")


def get_current_user(token: str = Depends(oauth2_scheme))-> AuthDto:
    return AuthService.decodeToken(token)
    


class AuthService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    @classmethod
    def generatePasswordHash(cls, password):
        return generate_password_hash(password)
    
    @classmethod
    def checkPasswordHash(cls, password, password_hash):
        return check_password_hash(password_hash, password)

    @classmethod
    def encodeTokens(cls, user: AuthDto) -> str:
        data = {
            'sender': 'SocialBeer',
            'created_at': str(datetime.datetime.now()),
            'user': user.username,
        }
        
        access_data = data
        refresh_data = data
        
        access_data['exp'] = str(datetime.datetime.now() + config.access_token_time)
        access_data['exp'] = str()
        return {
            'access_token': jwt.encode(payload = json_data, key = config.secret_access_token_key, algorithm="HS256"),
            'refresh_token': jwt.encode(payload = json_data, key = config.secret_refresh_token_key, algorithm="HS256"),
        } 
    
    
    @classmethod
    def decodeToken(cls, token: str) -> AuthDto:
        try:
            data = jwt.decode(jwt = token, key = config.secret_access_token_key, algorithms="HS256")
        except Exception as e:
            print(f"token is invalid {e}")

        user = AuthDto(username = data['user'], password_hash = data['password_hash'])   

        return user         


    def loginUser(self, authDto: AuthDto) ->str:
        user: UserModel = self.session.query(UserModel).filter_by(username = authDto.username).first()

        if not user or not self.checkPasswordHash(authDto.password, user.password_hash):
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED)
        
        return self.encodeTokens(AuthDto(username = user.username, password = user.password_hash))


    def registerUser(self, authDto: AuthDto):
        user = UserModel(
            username = authDto.username,
            password_hash = self.generatePasswordHash(authDto.password)
        )

        try:
            self.session.add(user)
            self.session.commit()
        except:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)
        
        return self.encodeTokens(AuthDto(
            username = user.username, 
            password = user.password_hash
        ))
    

    def refreshToken(self, refresh_token: str) -> str:
        try:
            data = jwt.decode(jwt = refresh_token, key = config.secret_refresh_token_key, algorithms="HS256")
        except Exception as e:
            print(f"token is invalid {e}")
            raise HTTPException(status_code = status.HTTP_403_FORBIDDEN)
        
        json_data = {
            'sender': 'SocialBeer',
            'date': str(datetime.datetime.now()),
            'user': data['user'],
            'password_hash': data['password_hash']
        }

        return {
            'access_token': jwt.encode(payload = json_data, key = config.secret_access_token_key, algorithm="HS256"),
            'refresh_token': jwt.encode(payload = json_data, key = config.secret_refresh_token_key, algorithm="HS256"),
        } 
        
        
