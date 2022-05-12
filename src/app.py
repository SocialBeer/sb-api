from turtle import title
from fastapi import FastAPI
from .users.controller import router as users_router


app = FastAPI(
    title = 'SB-Api'
)
app.include_router(users_router)