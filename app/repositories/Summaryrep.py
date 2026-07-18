from sqlalchemy.orm import Session
from app.models.Summary import Summary

def create_smy(smry:Summary,convoID:int,db:Session):
    db.add(smry)
    db.commit()
    db.refresh(smry)
    return smry
def get_all_Summary(convoID:int,userID:int,db:Session):
    return db.query(Summary).filter(Summary.ConversationID==convoID).all()

def get_recent_Summary(ConvoID:int,db:Session):
    return db.query(Summary).filter(Summary.ConversationID==ConvoID).order_by(Summary.SummaryDate.desc()).first()

def get_conversation_summaries(convoID:int, db:Session):

    return (
        db.query(Summary)
        .filter(
            Summary.ConversationID == convoID
        )
        .order_by(
            Summary.SummaryDate.asc()
        )
        .all()
    )