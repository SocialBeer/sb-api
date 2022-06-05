from werkzeug.security import generate_password_hash, check_password_hash
from fastapi import Depends, security, HTTPException, status
from sqlalchemy.orm import Session
import datetime
import jwt

from ..database import get_session
from .dto.token_dto import TokenDto
from .dto.login_dto import LoginDto
from .dto.register_dto import RegisterDto
from ..config import config
from ..users.model import UserModel


oauth2_scheme = security.OAuth2PasswordBearer(tokenUrl="/users/auth")

def get_current_user(token: str = Depends(oauth2_scheme)) -> LoginDto:
    return AuthService.decodeToken(token)
    
class AuthService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
    
    @staticmethod
    def encodeTokens(email: str) -> TokenDto:
        data = {
            'sender': 'SocialBeer',
            'created_at': str(datetime.datetime.now()),
            'email': email,
        }
        
        access_data = refresh_data = data
        
        access_data['exp'] = datetime.datetime.now() + config.access_token_time
        refresh_data['exp'] = datetime.datetime.now() + config.refresh_token_time

        return TokenDto(
            access_token = jwt.encode(payload = access_data, key = config.secret_access_token_key, algorithm="HS256"),
            refresh_token = jwt.encode(payload = refresh_data, key = config.secret_refresh_token_key, algorithm="HS256"),
        )
    
    @staticmethod
    def decodeToken(token: str) -> LoginDto:
        try:
            data = jwt.decode(jwt = token, key = config.secret_access_token_key, algorithms="HS256")
        except Exception as e:
            print(f"token is invalid {e}")

        user = LoginDto(email = data['email'], password_hash = data['password_hash'])   

        return user         

    def loginUser(self, loginDto: LoginDto) -> TokenDto:
        user: UserModel = self.session.query(UserModel).filter_by(email = loginDto.email).first()

        if not user or not check_password_hash(user.password_hash, loginDto.password):
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED)
        
        return self.encodeTokens(user.email)

    def registerUser(self, registerDto: RegisterDto) -> TokenDto:
        user = UserModel(
            email = registerDto.email,
            first_name = registerDto.first_name,
            last_name = registerDto.last_name,
            country = registerDto.country,
            password_hash = generate_password_hash(registerDto.password)
        )

        try:
            self.session.add(user)
            self.session.commit()
        except:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)
        
        return self.encodeTokens(user.email)
    
    def refreshToken(self, refresh_token: str) -> TokenDto:
        try:
            data = jwt.decode(jwt = refresh_token, key = config.secret_refresh_token_key, algorithms="HS256")
        except Exception as e:
            print(f"token is invalid {e}")
            raise HTTPException(status_code = status.HTTP_403_FORBIDDEN)
        
        return self.encodeTokens(data['email'])
        
        
