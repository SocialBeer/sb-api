from fastapi.security import HTTPBasic
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from .users.controller import router as users_router
from .auth.controller import router as auth_router

origins = [
    "http://localhost:3000",
]

app = FastAPI(
    title = 'SB-Api'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBasic()

app.include_router(users_router)
app.include_router(auth_router)