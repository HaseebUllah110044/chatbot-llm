from sqlalchemy import Column,String,Integer,DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database.database import Base
class Intent(Base):
    __tablename__="Intent"
    IntentID=Column(Integer,primary_key=True,index=True)
    IntentName=Column(String,nullable=False,unique=True)
    IntentDiscription=Column(String,nullable=False,unique=False)
    phrases=relationship("Phrase",back_populates="intent")
    responses=relationship("Response",back_populates="intent")