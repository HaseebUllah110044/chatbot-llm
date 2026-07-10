from app.models.User import User
from app.schemas.User import UserCreate,UserLogin
from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from app.dependencies.Security.hashpass import hashpass,verifyhash
from app.dependencies.Security.jwt import create_access_token
from app.repositories.User_repositories import get_by_email,get_by_username,RegiseterUser
from app.exceptions.custom_exceptions import InvalidCredentialException

def CreateUser(user:UserCreate,db:Session):
    UserModel=User()
    UserModel.UserName=user.UserName
    UserModel.UserEmail=user.UserEmail
    UserModel.UserPass=hashpass(user.UserPass)
    return RegiseterUser(UserModel,db)

def User_Login(user:UserLogin,db:Session):
    db_user=get_by_email(user.UserEmail,db)
    if db_user is None:
        raise InvalidCredentialException
    if verifyhash(user.UserPass,db_user.UserPass) ==False :
        raise InvalidCredentialException
    token=create_access_token(data={'sub':str(db_user.UserID),'Username':db_user.UserName})
    return {'access_token':token,'token_type':'bearer'}
        