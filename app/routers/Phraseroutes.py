from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.Phrase import PhraseCreate, PhraseUpdate, PhraseResponse
from app.services.Phraseservices import create_phrase_service, get_phrase_service, get_all_phrases_service, update_phrase_service, delete_phrase_service
from app.models.User import User
from app.dependencies.admin import admin_required


router = APIRouter(prefix="/admin/phrases", tags=["ADMIN"])


@router.post("/", response_model=PhraseResponse)
def create_phrase_route(payload: PhraseCreate, current_user: User = Depends(admin_required), db: Session = Depends(get_db)):
    return create_phrase_service(payload, db)


@router.get("/", response_model=list[PhraseResponse])
def get_all_phrase_route(current_user: User = Depends(admin_required), db: Session = Depends(get_db)):
    return get_all_phrases_service(db)


@router.get("/{phraseID}", response_model=PhraseResponse)
def get_phrase_route(phraseID: int, current_user: User = Depends(admin_required), db: Session = Depends(get_db)):
    return get_phrase_service(phraseID, db)


@router.put("/{phraseID}", response_model=PhraseResponse)
def update_phrase_route(phraseID: int, payload: PhraseUpdate, current_user: User = Depends(admin_required), db: Session = Depends(get_db)):
    return update_phrase_service(phraseID, payload, db)


@router.delete("/{phraseID}", status_code=status.HTTP_204_NO_CONTENT)
def delete_phrase_route(phraseID: int, current_user: User = Depends(admin_required), db: Session = Depends(get_db)):
    delete_phrase_service(phraseID, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)