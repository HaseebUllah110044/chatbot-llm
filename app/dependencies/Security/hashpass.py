from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def hashpass(password:str):
    return pwd_context.hash(password)
def verifyhash(plaintext,hash):
    pwd_context.verify(plaintext,hash)
