from sqlalchemy.orm import Session
from app.models.Message import Message

def create_msg(msg:Message,db:Session):
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg
def get_user_conversation(ConversationID:int,userID:int,db:Session):
    return db.query(Message).filter(Message.ConversationID==ConversationID).order_by(Message.MessageDateTime.asc()).all()
 
def get_recent_convo(ConvoID:int,userID:int,db:Session,limit:int=20):
    msgs= db.query(Message).filter(Message.ConversationID==ConvoID).order_by(Message.MessageDateTime.desc()).all()
    return msgs[::-1]


def get_count_msgs(convoID:int,EndMsg:int,db:Session):
    return db.query(Message).filter(Message.ConversationID==convoID,Message.MessageID>EndMsg).count()

def get_unsummarized_messages(convoID, last_summary_end_msg, db):
    return (
        db.query(Message)
        .filter(
            Message.ConversationID == convoID,
            Message.MessageID > last_summary_end_msg
        )
        .order_by(Message.MessageID.asc())
        .all()
    )
