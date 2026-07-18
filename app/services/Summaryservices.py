from sqlalchemy.orm import Session
from app.schemas.Summary import SummaryCreate,SummaryResponse
from app.models.Summary import Summary
from app.repositories.Massegerep import get_count_msgs,get_unsummarized_messages
from app.repositories.Summaryrep import create_smy,get_all_Summary,get_recent_Summary
from app.repositories.Conversationrep import get_conversation_id
from app.exceptions.custom_exceptions import usernotfoundException
from app.services.llmservice import llm_understand,generate_respone
from app.prompts.summary_prompts import SUMMARY_SYSTEM_PROMPT

def create_summary(payload:SummaryCreate,convoID:int,db:Session):
    sumary=Summary(
        ConversationID=payload.ConversationID,
        SummaryText=payload.SummaryText,
        StartMsg=payload.StartMsg,
        EndMsg=payload.EndMsg
        
    )
    return create_smy(sumary,convoID,db)

def get_summary(convoID:int,userID:int,db:Session):
    return get_all_Summary(convoID,userID,db)

def Current_Summary_Status(convoID:int,userID:int,db:Session):
    convo= get_conversation_id(convoID,db)
    if convo is None or convo.UserID != userID:
        raise usernotfoundException
    last_summary=get_recent_Summary(convoID,db)
    if last_summary is None : 
        msg_count=get_count_msgs(convoID,0,db)
    else:
        msg_count=get_count_msgs(convoID,last_summary.EndMsg,db)
    if msg_count >= 10:
        return True ,last_summary
    return False, 0
def Summary_generation(convoID:int,userID:int,db:Session):
    should_generate,last_summary=Current_Summary_Status(convoID,userID,db)
    if should_generate:
        if last_summary is None:
            history=get_unsummarized_messages(convoID,0,db)
        else:
            history=get_unsummarized_messages(convoID,last_summary.EndMsg,db)
        ai_context=llm_understand(history,SUMMARY_SYSTEM_PROMPT)
        SummaryTxt=generate_respone(ai_context)
        respone=SummaryCreate(ConversationID=convoID,SummaryText=SummaryTxt.message,StartMsg=history[0].MessageID,EndMsg=history[-1].MessageID)
        return create_summary(respone,convoID,db)
    return None