from sqlalchemy.orm import Session

from app.models.document import Document
from app.models.documnet_chunks import DocumentChunk



class DocumentRepository:


    def create_document(
        self,
        db: Session,
        title: str,
        name: str
    ):

        document = Document(
            DocTitle=title,
            DocName=name
        )

        db.add(document)
        db.flush()

        return document



    def create_chunk(
        self,
        db: Session,
        document_id: int,
        content: str,
        embedding: list[float],
        index: int,
        metadata: dict
    ):

        chunk = DocumentChunk(
            DocumentID=document_id,
            Content=content,
            Embedding=embedding,
            ChunkIndex=index,
            Metadata=metadata
        )

        db.add(chunk)

        return chunk



    def commit(
        self,
        db: Session
    ):

        db.commit()