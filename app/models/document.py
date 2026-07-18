from sqlalchemy import Column,Integer,String,DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database.database import Base

class Document(Base):
    __tablename__="documents"
    DocID=Column(Integer,primary_key=True,index=True)
    DocTitle=Column(String,nullable=False)
    DocName=Column(String,nullable=False)
    DocCreatedAt=Column(DateTime,default=datetime.utcnow,nullable=False)
    document_chunks=relationship("DocumentChunk",back_populates="documents")