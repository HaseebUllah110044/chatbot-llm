from sqlalchemy.orm import Session
import re 
from app.schemas.Phrase import PhraseResponse,UserResponse
from app.schemas.Response import ResponseResponse
from app.models.Intent import Intent
import random
from app.repositories.chatbot import get_intent_id,get_response_intentid,get_phrase_Msg,get_default_intent

def normalize_text(text: str):

    text = text.lower()
    text = text.strip()
    text = re.sub(r"[^\w\s]", "", text)

    return text

def IntentIDdetection(payload:UserResponse,db:Session):
    text=normalize_text(payload.PhraseText)
    phrase=get_phrase_Msg(text,db)
    if phrase is None:
        default_intent=get_default_intent(db)
        return PhraseResponse(PhraseID=None,
                          IntentID=default_intent.IntentID,
                          PhraseText="")

    return PhraseResponse(PhraseID=phrase.PhraseID,
                          IntentID=phrase.IntentID,
                          PhraseText=phrase.PhraseText)

def IntentDetection(payload:PhraseResponse,db:Session):
    intentID=payload.IntentID
    intent=get_intent_id(intentID,db)
    if intent is None:
        return get_default_intent(db)
    return intent
        
def BotResponse(intent:Intent,db:Session):
    response=get_response_intentid(intent.IntentID,db)
    if not response:
        intent=get_default_intent(db)
        response=get_response_intentid(intent.IntentID,db)
        final_response=random.choice(response)
        return ResponseResponse(ResponseID=final_response.ResponseID,
                                ResponseText=final_response.ResponseText,
                                IntentID=final_response.IntentID,
                                ResponseAccessLevel=final_response.ResponseAccessLevel
                                 )
    final_response=random.choice(response)
    return ResponseResponse(
        ResponseID=final_response.ResponseID,
        ResponseText=final_response.ResponseText,
        IntentID=final_response.IntentID,
        ResponseAccessLevel=final_response.ResponseAccessLevel
    )