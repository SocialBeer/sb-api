from fastapi import APIRouter, Depends

from .dto.login_dto import LoginDto
from .dto.register_dto import RegisterDto
from .service import AuthService
from .dto.token_dto import TokenDto


router = APIRouter(
    tags = ['Auth controller'],
    prefix = '/auth'
)

@router.post("/login")
def login_user(user: LoginDto, authService: AuthService = Depends()) -> TokenDto:
    return authService.loginUser(user)

@router.post("/registration")
def register_user(user: RegisterDto, authService: AuthService = Depends()) -> TokenDto:
    return authService.registerUser(user)

@router.post("/refresh-token/{refresh_token}")
def refresh_token(refresh_token: str, authService: AuthService = Depends()) -> TokenDto:
    return authService.refreshToken(refresh_token)