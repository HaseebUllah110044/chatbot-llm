from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends
from app.database.database import get_db
from app.models.User import User
from app.schemas.Summary import SummaryCreate,SummaryResponse
from app.dependencies.auth import current_user
from app.services.Summaryservices import create_smy,get_summary

router=APIRouter(prefix='/conversation/{convoID}',tags=['Masseges'])

@router.post("/", response_model=SummaryResponse)
def save_summary(
    convoID: int,
    payload: SummaryCreate,
    current_user: User = Depends(current_user),
    db: Session = Depends(get_db)
):
    return create_smy(payload,convoID,current_user.UserID,db)


@router.get("/", response_model=list[SummaryResponse])
def get_summary_route(
    convoID: int,
    current_user: User = Depends(current_user),
    db: Session = Depends(get_db)
):
    return get_summary( convoID, current_user.UserID,db)