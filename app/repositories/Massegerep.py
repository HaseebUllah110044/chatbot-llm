from sqlalchemy.orm import Session
from app.models.Message import Message

def create_msg(msg:Message,db:Session):
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg
def get_user_conversation(ConversationID:int,userID:int,db:Session):
    return db.query(Message).filter(Message.ConversationID==ConversationID).order_by(Message.MessageDateTime.asc()).all()
 
