from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends
from app.database.database import get_db
from app.models.User import User
from app.schemas.Phrase import UserResponse
from app.schemas.Masseges import CreateMassege,MassegeResponse
from app.services.Massegeservice import get_convo_history
from app.services.chat_handler import chat_handle
from app.dependencies.auth import current_user

router=APIRouter(prefix='/conversation/{convoID}',tags=['Masseges'])

@router.post("/", response_model=MassegeResponse)
def send_message_route(
    convoID: int,
    payload: UserResponse,
    current_user: User = Depends(current_user),
    db: Session = Depends(get_db)
):
    return chat_handle(payload,convoID,current_user.UserID,db)


@router.get("/", response_model=list[MassegeResponse])
def get_messages_route(
    convoID: int,
    current_user: User = Depends(current_user),
    db: Session = Depends(get_db)
):
    return get_convo_history( convoID, current_user.UserID,db)