from sqlalchemy.orm import Session
from app.models.User import User


def RegiseterUser(user:User,db:Session):
    db.add(user)
    db.commit()
    db.refresh(user)
    return {
        "message": f"User Registered Successfully, {user.UserName}"
    }

def get_by_username(username:str,db:Session):
   return db.query(User).filter(User.UserName==username).first()

def get_by_email(email:str,db:Session):
   return db.query(User).filter(User.UserEmail==email).first()

def get_by_id(userid:int,db:Session):
   return db.query(User).filter(User.UserID==userid).first()