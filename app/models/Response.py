from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database.database import Base
class Response(Base):
    __tablename__="Response"
    ResponseID=Column(Integer,primary_key=True,index=True)
    IntentID=Column(Integer,ForeignKey("Intent.IntentID"),nullable=False)
    ResponseText=Column(String,nullable=False,unique=False)
    ResponseAccessLevel=Column(String,default="Free")
    intent=relationship("Intent",back_populates="responses")