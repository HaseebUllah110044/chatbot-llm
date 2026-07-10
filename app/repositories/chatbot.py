from sqlalchemy.orm import Session
from app.models.Intent import Intent
from app.models.Phrase import Phrase
from app.models.Response import Response

def get_intent_id(intentID:int,db:Session):
    return db.query(Intent).filter(Intent.IntentID==intentID).first()
def get_response_intentid(intentID:int,db:Session):
    return db.query(Response).filter(Response.IntentID==intentID).all()
def get_phrase_Msg(msg:str,db:Session):
    return db.query(Phrase).filter(Phrase.PhraseText==msg).first()
def get_default_intent(db:Session):
    return db.query(Intent).filter(Intent.IntentName=="default").first()