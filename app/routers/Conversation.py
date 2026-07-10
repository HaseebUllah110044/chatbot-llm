from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.Conversation import ConversationCreate,ConversationResponse
from app.dependencies.auth import current_user
from app.models.User import User
from app.services.Conversationservice import create_convo,list_user_convo,get_convo
router=APIRouter(prefix='/conversation',tags=['Conversations'])

@router.post('/',response_model=ConversationResponse)
def creatconversation(payload:ConversationCreate,db:Session=Depends(get_db),currentuser:User=Depends(current_user)):
    return create_convo(db,currentuser.UserID,payload)
    
@router.get('/',response_model=list[ConversationResponse])    
def getconversationlist(db:Session=Depends(get_db),currentuser:User=Depends(current_user)):
    return list_user_convo(currentuser.UserID,db)

@router.get('/{convoID}',response_model=ConversationResponse)
def getconversation(convoID:int,db:Session=Depends(get_db),currentuser:User=Depends(current_user)):
    return get_convo(convoID,currentuser.userID,db)