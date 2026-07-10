from sqlalchemy.orm import Session
from app.models.Intent import Intent


def create_intent(intent: Intent, db: Session):
    db.add(intent)
    db.commit()
    db.refresh(intent)
    return intent


def get_intent_id(intentID: int, db: Session):
    return (
        db.query(Intent)
        .filter(Intent.IntentID == intentID)
        .first()
    )


def get_intent_name(intentName: str, db: Session):
    return (
        db.query(Intent)
        .filter(Intent.IntentName == intentName)
        .first()
    )


def get_all_intents(db: Session):
    return db.query(Intent).all()


def update_intent(intent: Intent, db: Session):
    db.commit()
    db.refresh(intent)
    return intent


def delete_intent(intent: Intent, db: Session):
    db.delete(intent)
    db.commit()