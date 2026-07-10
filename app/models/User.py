from sqlalchemy import Column,String,Integer,DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database.database import Base
class User(Base):
    __tablename__="User"
    UserID=Column(Integer,primary_key=True,index=True)
    UserName=Column(String,nullable=False,unique=True)
    UserEmail=Column(String,nullable=False,unique=True)
    UserPass=Column(String,nullable=False)
    UserRole=Column(String,default="Normal")
    UserCreationDate=Column(DateTime,default=datetime.utcnow)
    conversations=relationship("Conversation",back_populates="user")