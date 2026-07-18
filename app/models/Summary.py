from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database.database import Base
class Summary(Base):
    __tablename__="Summary"
    SummaryID=Column(Integer,primary_key=True,index=True)
    ConversationID=Column(Integer,ForeignKey("Conversation.ConversationID"),nullable=False)
    SummaryText=Column(String,nullable=False,unique=False)
    StartMsg=Column(Integer,ForeignKey("Message.MessageID"),nullable=False)
    EndMsg=Column(Integer,ForeignKey("Message.MessageID"),nullable=False)
    SummaryDate=Column(DateTime,default=datetime.utcnow)
    conversation=relationship("Conversation",back_populates="summaries")
    start_message = relationship(
    "Message",
    foreign_keys=[StartMsg],
    back_populates="start_summaries"
    )

    end_message = relationship(
    "Message",
    foreign_keys=[EndMsg],
    back_populates="end_summaries"
    )