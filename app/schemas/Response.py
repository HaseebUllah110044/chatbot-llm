from pydantic import BaseModel

class ResponseCreate(BaseModel):
    IntentID: int
    ResponseText: str
    ResponseAccessLevel: str


class ResponseUpdate(BaseModel):
    IntentID: int
    ResponseText: str
    ResponseAccessLevel: str
class ResponseResponse(BaseModel):
    ResponseID:int
    IntentID:int
    ResponseText:str
    ResponseAccessLevel:str
    class Config():
        from_attrrbute=True