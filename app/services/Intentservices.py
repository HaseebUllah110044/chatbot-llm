from sqlalchemy.orm import Session
from app.exceptions.custom_exceptions import IntentAlreadyExistsException,IntentNotFoundException
from app.models.Intent import Intent
from app.schemas.Intent import CreateIntent,IntentUpdate,IntentResponse
from app.repositories.Intentrep import create_intent,get_intent_id,get_intent_name,get_all_intents,update_intent,delete_intent
from app.services.ChatBot import normalize_text


def create_intent_service(payload: CreateIntent,db: Session):
    name = normalize_text(payload.IntentName)
    existing = get_intent_name(name, db)
    if existing:
        raise IntentAlreadyExistsException
    intent = Intent(
        IntentName=name,
        IntentDiscription=payload.IntentDiscription
    )
    intent = create_intent(intent, db)
    return IntentResponse(
        IntentID=intent.IntentID,
        IntentName=intent.IntentName,
        IntentDiscription=intent.IntentDiscription
    )


def get_intent_service(intentID: int,db: Session):
    intent = get_intent_id(intentID, db)
    if intent is None:
        raise IntentNotFoundException
    return IntentResponse(
        IntentID=intent.IntentID,
        IntentName=intent.IntentName,
        IntentDiscription=intent.IntentDiscription
    )


def get_all_intents_service(db: Session):
    return get_all_intents(db)


def update_intent_service(intentID: int,payload: IntentUpdate,db: Session):
    intent = get_intent_id(intentID, db)
    if intent is None:
        raise IntentNotFoundException

    name = normalize_text(payload.IntentName)

    duplicate = get_intent_name(name, db)

    if duplicate and duplicate.IntentID != intent.IntentID:
        raise IntentAlreadyExistsException

    intent.IntentName = name
    intent.IntentDiscription = payload.IntentDiscription

    intent = update_intent(intent, db)

    return IntentResponse(
        IntentID=intent.IntentID,
        IntentName=intent.IntentName,
        IntentDiscription=intent.IntentDiscription
    )


def delete_intent_service(intentID: int,db: Session):
    intent = get_intent_id(intentID, db)
    if intent is None:
        raise IntentNotFoundException
    delete_intent(intent, db)