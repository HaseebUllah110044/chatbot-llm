from sqlalchemy.orm import Session
from app.models.Phrase import Phrase
from app.exceptions.custom_exceptions import PhraseAlreadyExistsException,PhraseNotFoundException
from app.schemas.Phrase import PhraseCreate, PhraseUpdate, PhraseResponse
from app.repositories.phraserep import create_phrase, get_phrase_id, get_phrase_text, get_all_phrases, update_phrase, delete_phrase
from app.services.ChatBot import normalize_text


def create_phrase_service(payload: PhraseCreate, db: Session):

    text = normalize_text(payload.PhraseText)

    existing = get_phrase_text(text, db)

    if existing:
        raise PhraseAlreadyExistsException

    phrase = Phrase(
        IntentID=payload.IntentID,
        PhraseText=text
    )

    return create_phrase(phrase, db)


def get_phrase_service(phraseID: int, db: Session):

    phrase = get_phrase_id(phraseID, db)

    if phrase is None:
        raise PhraseNotFoundException

    return phrase


def get_all_phrases_service(db: Session):
    return get_all_phrases(db)


def update_phrase_service(phraseID: int, payload: PhraseUpdate, db: Session):

    phrase = get_phrase_id(phraseID, db)

    if phrase is None:
        raise PhraseNotFoundException

    text = normalize_text(payload.PhraseText)

    duplicate = get_phrase_text(text, db)

    if duplicate and duplicate.PhraseID != phrase.PhraseID:
        raise PhraseAlreadyExistsException

    phrase.IntentID = payload.IntentID
    phrase.PhraseText = text

    return update_phrase(phrase, db)


def delete_phrase_service(phraseID: int, db: Session):

    phrase = get_phrase_id(phraseID, db)

    if phrase is None:
        raise PhraseNotFoundException

    delete_phrase(phrase, db)