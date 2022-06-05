from pydantic import BaseModel
from typing import Any

from ..model import UserModel


class ResponseUserDto(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    country: str