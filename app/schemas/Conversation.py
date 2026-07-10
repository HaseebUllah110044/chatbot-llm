from pydantic import BaseModel
from datetime import datetime
from app.schemas.Masseges import MassegeResponse
class ConversationCreate(BaseModel):
    ConversationTitle:str
class ConversationResponse(BaseModel):
    ConversationID:int
    UserID:int
    ConversationTitle:str
    ConversationDateTime:datetime
    class Config:
        from_attributes=True


