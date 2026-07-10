from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.Response import ResponseCreate, ResponseUpdate, ResponseResponse
from app.services.Responseservices import create_response_service, get_response_service, get_all_response_service, update_response_service, delete_response_service
from app.models.User import User
from app.dependencies.admin import admin_required


router = APIRouter(prefix="/admin/responses", tags=["ADMIN"])


@router.post("/", response_model=ResponseResponse)
def create_response_route(payload: ResponseCreate, current_user: User = Depends(admin_required), db: Session = Depends(get_db)):
    return create_response_service(payload, db)


@router.get("/", response_model=list[ResponseResponse])
def get_responses_route(current_user: User = Depends(admin_required), db: Session = Depends(get_db)):
    return get_all_response_service(db)


@router.get("/{responseID}", response_model=ResponseResponse)
def get_response_route(responseID: int, current_user: User = Depends(admin_required), db: Session = Depends(get_db)):
    return get_response_service(responseID, db)


@router.put("/{responseID}", response_model=ResponseResponse)
def update_response_route(responseID: int, payload: ResponseUpdate, current_user: User = Depends(admin_required), db: Session = Depends(get_db)):
    return update_response_service(responseID, payload, db)


@router.delete("/{responseID}", status_code=status.HTTP_204_NO_CONTENT)
def delete_response_route(responseID: int, current_user: User = Depends(admin_required), db: Session = Depends(get_db)):
    delete_response_service(responseID, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)