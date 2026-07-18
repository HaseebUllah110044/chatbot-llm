from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.ingestion_Service import IngestionService


ingest_service = IngestionService()

router = APIRouter(
    prefix='/ingestion'
)


@router.post("/ingest")
def ingest_documents(
    folder_path: str,
    db: Session = Depends(get_db)
):

    return ingest_service.ingest_folder(
        folder_path,
        db
    )