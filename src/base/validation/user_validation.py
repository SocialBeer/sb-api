from fastapi import HTTPException, status
from pydantic import BaseModel, validator
import re
 

class BaseValidation(BaseModel):

    @classmethod
    def __validation_function(cls, value: str, regx: str, min: int, max: int, error_msg: str):
        if re.match(regx, value) is None or len(value) < min or len(value) > max:
            raise HTTPException(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY, detail = {'msg': error_msg})
        
        return value
    
    @validator('first_name', 'last_name', 'country', check_fields = False)
    def information_fields_validation(cls, field: str):
        return cls.__validation_function(
            field, 
            "^[a-zA-Z]+$", 
            3, 20, 
            "validation error"
        )
    
    @validator('password', check_fields = False)
    def password_validation(cls, password: str):
        return cls.__validation_function(
            password, 
            "((?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{6,20})", 
            6, 20, 
            "password validation error"
        )

    @validator('email', check_fields = False)
    def email_validation(cls, email: str):
        return cls.__validation_function(
            email, 
            "^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$", 
            6, 20, 
            "email validation error"
        )
