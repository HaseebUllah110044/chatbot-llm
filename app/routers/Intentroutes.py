from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.Intent import CreateIntent,IntentUpdate,IntentResponse
from app.services.Intentservices import create_intent_service,get_intent_service,get_all_intents_service,update_intent_service,delete_intent_service
from app.models.User import User
from app.dependencies.admin import admin_required

router = APIRouter(prefix="/admin/intent",tags=["ADMIN"])
@router.post("/",response_model=IntentResponse)
def create_intent_route(payload: CreateIntent,current_user: User = Depends(admin_required),db: Session = Depends(get_db)):
    return create_intent_service(payload,db)

@router.get("/",response_model=list[IntentResponse])
def get_all_intents_route(current_user: User = Depends(admin_required),db: Session = Depends(get_db)):
    return get_all_intents_service(db)


@router.get("/{intentID}",response_model=IntentResponse)
def get_intent_route(intentID: int,current_user: User = Depends(admin_required),db: Session = Depends(get_db)):
    return get_intent_service(intentID,db)


@router.patch("/{intentID}",response_model=IntentResponse)
def update_intent_route(intentID: int,payload: IntentUpdate,current_user: User = Depends(admin_required),db: Session = Depends(get_db)):
    return update_intent_service(intentID,payload,db)

@router.delete("/{intentID}")
def delete_intent_route(intentID: int,current_user: User = Depends(admin_required),db: Session = Depends(get_db)):
    return delete_intent_service(intentID,db)