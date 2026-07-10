from sqlalchemy.orm import Session
from app.models.Phrase import Phrase


def create_phrase(phrase: Phrase, db: Session):
    db.add(phrase)
    db.commit()
    db.refresh(phrase)
    return phrase


def get_phrase_id(phraseID: int, db: Session):
    return db.query(Phrase).filter(Phrase.PhraseID == phraseID).first()


def get_phrase_text(text: str, db: Session):
    return db.query(Phrase).filter(Phrase.PhraseText == text).first()


def get_all_phrases(db: Session):
    return db.query(Phrase).all()


def update_phrase(phrase: Phrase, db: Session):
    db.commit()
    db.refresh(phrase)
    return phrase


def delete_phrase(phrase: Phrase, db: Session):
    db.delete(phrase)
    db.commit()