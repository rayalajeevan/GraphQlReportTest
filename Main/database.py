from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,scoped_session
from .settings import get_settings

settings=get_settings()
def get_database_url():
    return 'postgresql://{}:{}@{}:{}/{}'.format(settings.database_user, settings.database_password,
                                                settings.database_host, settings.database_port, "reportsdb")


DATABASE_URL = get_database_url()
engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.query=scoped_session(SessionLocal).query_property()