from pydantic import BaseModel

class SummaryCreate(BaseModel):
    ConversationID:int
    SummaryText: str
    StartMsg:int
    EndMsg:int
    

class SummaryResponse(BaseModel):
    SummaryID: int
    ConversationID:int
    SummaryText: str
    StartMsg:int
    EndMsg:int
    class Config():
        from_attrrbute=True