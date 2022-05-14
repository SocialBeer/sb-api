from fastapi import APIRouter, Depends

from src.auth.dto.auth_dto import AuthDto
from src.auth.service import AuthService


router = APIRouter(
    tags = ['Auth controller'],
    prefix = '/auth'
)

@router.post("/login")
def login_user(user: AuthDto, authService: AuthService = Depends()):
    return authService.loginUser(user)


@router.post("/registration")
def register_user(user: AuthDto, authService: AuthService = Depends()):
    return authService.registerUser(user)


@router.post("/refresh-token/{refresh_token}")
def refresh_token(refresh_token: str, authService: AuthService = Depends()):
    return authService.refreshToken(refresh_token)