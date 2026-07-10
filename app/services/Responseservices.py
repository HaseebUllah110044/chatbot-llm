from sqlalchemy.orm import Session
from app.models.Response import Response
from app.exceptions.custom_exceptions import ResponseNotFoundException
from app.schemas.Response import ResponseCreate, ResponseUpdate
from app.repositories.Responserep import create_response, get_response_id, get_all_responses, update_response, delete_response


def create_response_service(payload: ResponseCreate, db: Session):

    response = Response(
        IntentID=payload.IntentID,
        ResponseText=payload.ResponseText,
        ResponseAccessLevel=payload.ResponseAccessLevel
    )

    return create_response(response, db)


def get_response_service(responseID: int, db: Session):

    response = get_response_id(responseID, db)

    if response is None:
        raise ResponseNotFoundException

    return response


def get_all_response_service(db: Session):
    return get_all_responses(db)


def update_response_service(responseID: int, payload: ResponseUpdate, db: Session):

    response = get_response_id(responseID, db)

    if response is None:
        raise ResponseNotFoundException

    response.IntentID = payload.IntentID
    response.ResponseText = payload.ResponseText
    response.ResponseAccessLevel = payload.ResponseAccessLevel

    return update_response(response, db)


def delete_response_service(responseID: int, db: Session):

    response = get_response_id(responseID, db)

    if response is None:
        raise ResponseNotFoundException

    delete_response(response, db)