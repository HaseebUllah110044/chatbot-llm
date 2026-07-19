from sqlalchemy.orm import Session
from app.services.Massegeservice import send_bot_msg,send_user_msg
from app.repositories.Conversationrep import get_conversation_id
from app.schemas.Phrase import UserResponse
from app.exceptions.custom_exceptions import ConvoNotFoundException
from app.schemas.Masseges import CreateMassege
from app.services.llmservice import generate_respone
from app.services.Summaryservices import Summary_generation
from app.services.context_service import context_builder
from app.prompts.chat_prompts import CHAT_SYSTEM_PROMPT
from app.services.tokenservices import count_token

fallback=CreateMassege(Massegetxt="Sorry i didn't understand that.")

def chat_handle(payload:UserResponse,convoID:int,userID:int,db:Session):
    convo=get_conversation_id(convoID,db)
    if convo is None or convo.UserID != userID:
        raise ConvoNotFoundException
    send_user_msg(convoID,payload.PhraseText,db)
    ai_context=context_builder(payload.PhraseText,convoID,userID,db)
    ai_context.append({
        "role":"user",
        "content":payload.PhraseText
    })
    count=count_token(ai_context)
    print(count)
    bot=generate_respone(ai_context)
    bot_msg=send_bot_msg(convoID,bot.message,db)
    Summary_generation(convoID,userID,db)
    return bot_msg

    
    
    