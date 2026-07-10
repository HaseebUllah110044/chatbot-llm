from pydantic import BaseModel
from datetime import datetime

class CreateMassege(BaseModel):
    Massegetxt:str
    
class MassegeResponse(BaseModel):
    MessageID:int
    ConversationID:int
    MessageText:str
    MessageSender:str
    MessageDateTime:datetime
    class Config():
        from_attributes=True