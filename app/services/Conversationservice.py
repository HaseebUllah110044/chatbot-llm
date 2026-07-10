from sqlalchemy.orm import Session
from typing import Optional
from app.exceptions.custom_exceptions import ConvoNotFoundException
from app.models.Conversation import Conversation
from app.schemas.Conversation import ConversationCreate
from app.repositories.Conversationrep import create_conversation,get_conversation_id,get_conversation_user

def create_convo(db: Session,userID:int,payload: ConversationCreate):
    conversation = Conversation(
        UserID=userID,
        ConversationTitle=payload.ConversationTitle
    )
    return create_conversation(conversation, db)
def get_convo(convoID:int,userID:int,db:Session):
    convo= get_conversation_id(convoID,db)
    if convo is None or convo.UserID != userID:
        raise ConvoNotFoundException
    return convo
def list_user_convo(userID:int,db:Session):
    return get_conversation_user(userID,db)
