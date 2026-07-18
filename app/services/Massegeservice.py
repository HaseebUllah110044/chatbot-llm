from sqlalchemy.orm import Session
from app.models.Message import Message
from app.schemas.Masseges import CreateMassege
from app.repositories.Massegerep import create_msg,get_user_conversation,get_recent_convo
from app.repositories.User_repositories import get_by_id
from datetime import datetime

def send_user_msg(convoID:int,msgtxt:str,db:Session):
    msg=Message(
        ConversationID=convoID,
        MessageSender="user",
        MessageText=msgtxt 
    )
    return create_msg(msg,db)

def send_bot_msg(convoID:int,msgtxt:str,db:Session):
    msg=Message(
        ConversationID=convoID,
        MessageSender="bot",
        MessageText=msgtxt       
    )
    return create_msg(msg,db)
def get_convo_history(convoID:int,userID:int,db:Session):
    return get_user_conversation(convoID,userID,db)
def recent_msgs(convoID:int,userID:int,db:Session,limit:int):
    return get_recent_convo(convoID,userID,db,limit)

