from sqlalchemy.orm import Session
from app.prompts.chat_prompts import CHAT_SYSTEM_PROMPT
from app.repositories.Summaryrep import get_conversation_summaries
from app.services.Massegeservice import recent_msgs
from app.models.Summary import Summary
from app.models.Message import Message
from app.services.tokenservices import count_token


def context_builder(convoID:int,userID:int,db:Session):
    history_msgs=recent_msgs(convoID,userID,db,limit=5)
    history_summary=get_conversation_summaries(convoID,db)
    ai_context=context_ai(history_msgs,history_summary,CHAT_SYSTEM_PROMPT)
    return ai_context
    
def context_ai(Msg:list[Message],Smry:list[Summary],prompt:str,max_token:int=3000):
    context = [
        {
            "role": "system",
            "content": prompt
        }
    ]
    current_token=count_token(context)
    for summaries in reversed(Smry):
        summary_msg=({
                "role":"system",
                "content":
                 f"Previous conversation summary:\n{summaries.SummaryText}"
            })
        summary_token=count_token([summary_msg])
        if current_token+summary_token>max_token:
            break
        context.append(summary_msg)
        current_token+=summary_token
    for msg in reversed(Msg):
        
        if msg.MessageSender == 'user':
            msg.MessageSender='user'
        else:
            msg.MessageSender='assistant'
        messages=({
            "role":msg.MessageSender,
            "content":msg.MessageText
        })
        msg_token=count_token([messages])
        if current_token+msg_token>max_token:
            break
        context.append(messages)
        current_token+=msg_token
    return context
