from pydantic_settings import BaseSettings

class Setting(BaseSettings):

    DATABASE_URL:str
    SECRET_KEY:str
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int
    OPENAI_API_KEY:str
    EMBEDDING_MODEL:str
    EMBEDDING_DIMENSION:int
    class Config:
        env_file = ".env"
        
setting=Setting()