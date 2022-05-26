from fastapi import APIRouter, Depends

from .dto.auth_dto import AuthDto
from .service import AuthService
from .dto.token_dto import TokenDto


router = APIRouter(
    tags = ['Auth controller'],
    prefix = '/auth'
)

@router.post("/login")
def login_user(user: AuthDto, authService: AuthService = Depends()) -> TokenDto:
    return authService.loginUser(user)

@router.post("/registration")
def register_user(user: AuthDto, authService: AuthService = Depends()) -> TokenDto:
    return authService.registerUser(user)

@router.post("/refresh-token/{refresh_token}")
def refresh_token(refresh_token: str, authService: AuthService = Depends()) -> TokenDto:
    return authService.refreshToken(refresh_token)