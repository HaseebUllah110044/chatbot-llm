from pathlib import Path
from sqlalchemy.orm import Session

from app.ingestion.loader.Json_loader import WebsiteJSONLoader
from app.ingestion.chunker.baseline_chunker import TextChunker
from app.services.embeddingservice import EmbeddingService
from app.repositories.documnetrepo import DocumentRepository


class IngestionService:

    def __init__(self):
        self.loader = WebsiteJSONLoader()
        self.chunker = TextChunker()
        self.embedding = EmbeddingService()
        self.repository = DocumentRepository()


    def ingest(
        self,
        filepath: str,
        db: Session
    ):

        document_data = self.loader.load(filepath)


        document = self.repository.create_document(
            db,
            title=document_data["title"],
            name=filepath
        )


        chunks = self.chunker.chunk(
            document_data["content"]
        )


        metadata = {
            "url": document_data["url"],
            "title": document_data["title"]
        }


        for chunk in chunks:

            vector = self.embedding.create_embedding(
                chunk["content"]
            )


            self.repository.create_chunk(
                db,
                document.DocID,
                chunk["content"],
                vector,
                chunk["index"],
                metadata
            )


        self.repository.commit(db)


        return {
            "document_id": document.DocID,
            "chunks": len(chunks)
        }



    def ingest_folder(
        self,
        folder_path: str,
        db: Session
    ):

        folder = Path(folder_path)

        results = []


        for filepath in folder.glob("*.json"):

            print(f"Ingesting: {filepath.name}")


            result = self.ingest(
                str(filepath),
                db
            )


            results.append({
                "file": filepath.name,
                **result
            })


        return results