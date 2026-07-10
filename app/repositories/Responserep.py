from sqlalchemy.orm import Session
from app.models.Response import Response


def create_response(response: Response, db: Session):
    db.add(response)
    db.commit()
    db.refresh(response)
    return response


def get_response_id(responseID: int, db: Session):
    return db.query(Response).filter(Response.ResponseID == responseID).first()


def get_all_responses(db: Session):
    return db.query(Response).all()


def update_response(response: Response, db: Session):
    db.commit()
    db.refresh(response)
    return response


def delete_response(response: Response, db: Session):
    db.delete(response)
    db.commit()