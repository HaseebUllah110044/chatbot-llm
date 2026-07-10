from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi import status

from app.exceptions.custom_exceptions import NotAdminException,ResponseNotFoundException,PhraseAlreadyExistsException,PhraseNotFoundException,usernotfoundException,UseralreadyexsistException,ConvoNotFoundException,InvalidCredentialException,IntentAlreadyExistsException,IntentNotFoundException

async def user_notfound_handler(request:Request,exc:usernotfoundException):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={"detail":"User Not Found"})

async def user_exsist_handler(request:Request,exc:UseralreadyexsistException):
    return JSONResponse(status_code=status.HTTP_409_CONFLICT,content={"detail":"User Already Exsists"})

async def invalid_credentials_handler(request:Request,exc:InvalidCredentialException):
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,content={"detail":"User Not Found"})

async def convoNotFound_handler(request:Request,exc:ConvoNotFoundException):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={"detail":"Conversation Not Found"})

async def IntentAlready_handler(request:Request,exc:IntentAlreadyExistsException):
    return JSONResponse(status_code=status.HTTP_409_CONFLICT,content={"detail":"Intent Already Exsist"})

async def IntentNotFound_handler(request:Request,exc:IntentNotFoundException):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={"detail":"Intent Not Found"})
async def PhraseAlready_handler(request:Request,exc:PhraseAlreadyExistsException):
    return JSONResponse(status_code=status.HTTP_409_CONFLICT,content={"detail":"Phrase Already Exsist"})

async def PhraseNotFound_handler(request:Request,exc:PhraseNotFoundException):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={"detail":"Phrase Not Found"})

async def ResponseNotFound_handler(request:Request,exc:ResponseNotFoundException):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={"detail":"Response Not Found"})

async def NotAdmin_handler(request:Request,exc:NotAdminException):
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,content={"detail":"UnAuthorized Individual"})