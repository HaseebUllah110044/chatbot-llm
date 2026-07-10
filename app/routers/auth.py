from fastapi import APIRouter
from app.schemas.User import UserCreate,UserLogin,UserResponse,token_sch
from app.services.Userservices import CreateUser,User_Login
from app.database.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import status
from app.dependencies.auth import current_user
router=APIRouter(prefix="/auth",tags=["Authentication"])

@router.post('/register',status_code=status.HTTP_201_CREATED)
def register(user:UserCreate,db:Session=Depends(get_db)):
    return CreateUser(user,db)

@router.post('/login',status_code=status.HTTP_200_OK,response_model=token_sch)
def login(user:UserLogin,db:Session=Depends(get_db)):
    return User_Login(user,db)

@router.get('/profile',response_model=UserResponse,status_code=status.HTTP_202_ACCEPTED)
def profile(current_profile=Depends(current_user)):
    return current_profile