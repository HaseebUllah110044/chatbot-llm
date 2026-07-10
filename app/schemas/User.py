from pydantic import BaseModel,EmailStr,field_validator
import re

class UserCreate(BaseModel):
    UserName:str;
    UserEmail:EmailStr;
    UserPass:str;
    @field_validator("UserName")
    def Validate_Username(cls,value):
        if not re.match(r'^[a-zA-Z0-9_]+$',value):
            raise ValueError("Invalid Username")
        return value
    @field_validator("UserPass")
    def Validate_Email(cls,value):
        if len(value) < 8:
            raise ValueError("Password should contain 8 or more characters")
        return value
    
class UserLogin(BaseModel):
    UserEmail:EmailStr
    UserPass:str
class token_sch(BaseModel):
    access_token:str
    token_type:str
    class Config():
        from_attributes=True
class UserResponse(BaseModel):
    UserID:int
    UserName:str
    UserEmail:EmailStr
    UserRole:str
    class Config():
        from_attributes=True;