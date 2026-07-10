from sqlalchemy.orm import Session
from app.services.ChatBot import IntentIDdetection,IntentDetection,BotResponse
from app.services.Massegeservice import send_bot_msg,send_user_msg
from app.repositories.Conversationrep import get_conversation_id
from app.schemas.Phrase import UserResponse
from app.exceptions.custom_exceptions import ConvoNotFoundException
from app.schemas.Masseges import CreateMassege

fallback=CreateMassege(Massegetxt="Sorry i didn't understand that.")

def bot_functionality(payload:UserResponse,db:Session):
    phrase=IntentIDdetection(payload,db)
    intent=IntentDetection(phrase,db)
    response=BotResponse(intent,db)
    return response    

def chat_handle(payload:UserResponse,convoID:int,userID:int,db:Session):
    convo=get_conversation_id(convoID,db)
    if convo is None or convo.UserID != userID:
        raise ConvoNotFoundException
    send_user_msg(convoID,payload.PhraseText,db)
    bot=bot_functionality(payload,db)
    return send_bot_msg(convoID,bot.ResponseText,db)
    
    
    