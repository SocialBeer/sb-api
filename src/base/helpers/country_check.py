import json
from typing import Union
from fastapi import HTTPException, status

from src.auth.dto.register_dto import RegisterDto
from src.users.dto.create_user_dto import CreateUserDto


async def country_check(createUserDto: CreateUserDto):
    with open("src/assets/countries.json") as json_file:
        json_data = list(json.load(json_file))
        if createUserDto.country not in json_data:
            raise HTTPException(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY, detail = {'msg': "country does't exists"})
    
    return createUserDto
