from sqlalchemy import Column, Integer, DateTime, ForeignKey, JSON,Text
from datetime import datetime
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector


from app.database.database import Base


class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    ChunkID = Column(
        Integer,
        primary_key=True,
        index=True
    )

    DocumentID = Column(
        Integer,
        ForeignKey("documents.DocID"),
        nullable=False
    )

    Content = Column(
        Text,
        nullable=False
    )

    Embedding = Column(
        Vector(512),
        nullable=False
    )

    ChunkIndex = Column(
        Integer,
        nullable=False
    )

    Metadata = Column(
        JSON,
        nullable=True
    )

    ChunkCreatedAt = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )
    documents=relationship("Document",back_populates="document_chunks")