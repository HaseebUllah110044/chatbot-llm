from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database.database import Base
class Phrase(Base):
    __tablename__="Phrase"
    PhraseID=Column(Integer,primary_key=True,index=True)
    IntentID=Column(Integer,ForeignKey("Intent.IntentID"),nullable=False)
    PhraseText=Column(String,nullable=False,unique=False)
    intent=relationship("Intent",back_populates="phrases")