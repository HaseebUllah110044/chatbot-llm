from sqlalchemy.orm import Session
from app.models.Conversation import Conversation

def create_conversation(conversation:Conversation,db:Session):
    db.add(conversation)
    db.commit()
    db.refresh(conversation)
    return conversation
def get_conversation_id(ConversationID:int,db:Session):
    return db.query(Conversation).filter(Conversation.ConversationID==ConversationID).first()
def get_conversation_user(UserID:int,db:Session):
    return db.query(Conversation).filter(Conversation.UserID==UserID).all()