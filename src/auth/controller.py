from fastapi import APIRouter, Depends

from .dto.register_metadata_dto import RegisterMetaData
from .dto.login_dto import LoginDto
from .dto.register_dto import RegisterDto
from .service import AuthService
from .dto.token_dto import TokenDto
from src.base.helpers.country_check import country_check


router = APIRouter(
    tags = ['Auth controller'],
    prefix = '/auth'
)

@router.post("/login")
def login_user(user: LoginDto, authService: AuthService = Depends()) -> TokenDto:
    return authService.loginUser(user)

@router.post("/registration")
def register_user(authService: AuthService = Depends(), user = Depends(country_check)) -> TokenDto:
    return authService.registerUser(user)

@router.post("/refresh-token/{refresh_token}")
def refresh_token(refresh_token: str, authService: AuthService = Depends()) -> TokenDto:
    return authService.refreshToken(refresh_token)

@router.get("/registration/metadata")
def get_metadata(authService: AuthService = Depends()) -> RegisterMetaData:
    return authService.getMetadata()