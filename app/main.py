from fastapi import FastAPI
from app.routers.auth import router as auth_router
from app.exceptions.globalhandler import (user_notfound_handler,user_exsist_handler,invalid_credentials_handler
,convoNotFound_handler,IntentAlready_handler,IntentNotFound_handler,PhraseAlready_handler,PhraseNotFound_handler,
ResponseNotFound_handler,NotAdmin_handler)
from app.exceptions.custom_exceptions import (usernotfoundException,UseralreadyexsistException,InvalidCredentialException,
ConvoNotFoundException,IntentAlreadyExistsException,IntentNotFoundException,PhraseAlreadyExistsException,
PhraseNotFoundException,ResponseNotFoundException,NotAdminException)
from app.routers.Conversation import router as convo_router
from app.routers.ingestionroute import router as ingestion_router
from app.routers.Massege import router as msg_router
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()
@app.get("/health")
def health_check():
    return {"status": "ok"}
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173","https://suparco-frontend-mu.vercel.app"], allow_methods=["*"], allow_headers=["*"])
app.include_router(auth_router)
app.include_router(convo_router)
app.include_router(msg_router)
app.include_router(ingestion_router)
app.add_exception_handler(usernotfoundException,user_notfound_handler)
app.add_exception_handler(UseralreadyexsistException,user_exsist_handler)
app.add_exception_handler(InvalidCredentialException,invalid_credentials_handler)
app.add_exception_handler(ConvoNotFoundException,convoNotFound_handler)
app.add_exception_handler(IntentAlreadyExistsException,IntentAlready_handler)
app.add_exception_handler(IntentNotFoundException,IntentNotFound_handler)
app.add_exception_handler(PhraseAlreadyExistsException,PhraseAlready_handler)
app.add_exception_handler(PhraseNotFoundException,PhraseNotFound_handler)
app.add_exception_handler(ResponseNotFoundException,ResponseNotFound_handler)
app.add_exception_handler(NotAdminException,NotAdmin_handler)
