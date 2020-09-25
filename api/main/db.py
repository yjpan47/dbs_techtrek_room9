from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from api.main.config import DB_ENGINE_URL

DB_ENGINE = create_engine(DB_ENGINE_URL, pool_size=20, max_overflow=100)
Session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=DB_ENGINE))
