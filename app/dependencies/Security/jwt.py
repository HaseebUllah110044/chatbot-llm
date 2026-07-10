from jose import jwt,JWTError
from datetime  import datetime,timedelta
from app.core.config import setting

def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp':expire})
    return jwt.encode(to_encode,setting.SECRET_KEY,algorithm=setting.ALGORITHM)

def decode_access_token(token:str):
    try:
        payload=jwt.decode(token,setting.SECRET_KEY,algorithms=setting.ALGORITHM)
        return payload
    except JWTError:
        return None