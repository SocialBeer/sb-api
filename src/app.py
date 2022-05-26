from fastapi.security import HTTPBasic
from fastapi import FastAPI

from .users.controller import router as users_router
from .auth.controller import router as auth_router



app = FastAPI(
    title = 'SB-Api'
)

security = HTTPBasic()

app.include_router(users_router)
app.include_router(auth_router)