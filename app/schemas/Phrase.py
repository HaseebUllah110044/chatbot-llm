from pydantic import BaseModel
class UserResponse(BaseModel):
    PhraseText:str

class PhraseCreate(BaseModel):
    IntentID: int
    PhraseText: str

class PhraseUpdate(BaseModel):
    IntentID: int
    PhraseText: str

class PhraseResponse(BaseModel):
    PhraseID:int | None=None
    IntentID:int
    PhraseText:str
    class Config():
        from_attributes=True