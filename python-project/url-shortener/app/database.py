
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings


# Create the database engine
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
)


# Create a session factory
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


# Base class for all database models
class Base(DeclarativeBase):
    pass


# Provide a database session to each request
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
