from pydantic import BaseModel
from typing import Optional

class CreateIntent(BaseModel):
    IntentName:str
    IntentDiscription:str
    
class IntentUpdate(BaseModel):
    IntentName: Optional[str] = None
    IntentDiscription: Optional[str] = None
    
class IntentResponse(BaseModel):
    IntentID:int
    IntentName:str
    IntentDiscription:str
    class Config():
        from_attributes=True