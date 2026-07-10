from fastapi import HTTPException,Depends
from sqlalchemy.orm import Session
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from app.database.database import get_db
from app.dependencies.Security.jwt import decode_access_token
from app.repositories.User_repositories import get_by_id
from app.exceptions.custom_exceptions import InvalidCredentialException,usernotfoundException

security=HTTPBearer()
def current_user(credentials:HTTPAuthorizationCredentials=Depends(security),db:Session=Depends(get_db)):
    token=credentials.credentials
    payload=decode_access_token(token)
    if payload is None:
        raise InvalidCredentialException
    userid=payload.get('sub')
    if userid is None:
        raise InvalidCredentialException
    user=get_by_id(userid,db)
    if user is None:
        raise usernotfoundException
    return user