from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database.database import Base
class Conversation(Base):
    __tablename__="Conversation"
    ConversationID=Column(Integer,primary_key=True,index=True)
    UserID=Column(Integer,ForeignKey("User.UserID"),nullable=False)
    ConversationTitle=Column(String,nullable=False,unique=False)
    ConversationDateTime=Column(DateTime,default=datetime.utcnow)
    user=relationship("User",back_populates="conversations")
    messages=relationship("Message",back_populates="conversation")