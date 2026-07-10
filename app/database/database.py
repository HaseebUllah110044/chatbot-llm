from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base
from app.core.config import setting

engine=create_engine(setting.DATABASE_URL,connect_args={"check_same_thread":False})

Sessionlocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()


def get_db():
    db=Sessionlocal()
    try:
        yield db
    finally:
        db.close()