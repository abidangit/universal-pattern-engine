"""Database session helpers for UPE."""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///upe.db')

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def init_db():
    from .models import Base
    Base.metadata.create_all(bind=engine)

def get_session():
    return SessionLocal()
