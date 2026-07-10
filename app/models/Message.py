from sqlalchemy import Column,String,Integer,DateTime,ForeignKey,Text
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database.database import Base
class Message(Base):
    __tablename__="Message"
    MessageID=Column(Integer,primary_key=True,index=True)
    ConversationID=Column(Integer,ForeignKey("Conversation.ConversationID"),nullable=False)
    MessageSender=Column(String,nullable=False,unique=False)
    MessageText=Column(Text,nullable=False,unique=False)
    MessageDateTime=Column(DateTime,default=datetime.utcnow)
    conversation=relationship("Conversation",back_populates="messages")