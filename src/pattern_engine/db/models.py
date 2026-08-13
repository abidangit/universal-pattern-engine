"""SQLAlchemy models for Universal Pattern Engine."""
from sqlalchemy import Column, Integer, String, Float, JSON, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Pattern(Base):
    __tablename__ = 'patterns'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    category = Column(String(100), nullable=True)
    parameters = Column(JSON, nullable=True)
    initial_conditions = Column(JSON, nullable=True)
    metadata = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class ExperimentResult(Base):
    __tablename__ = 'experiment_results'
    id = Column(Integer, primary_key=True)
    experiment_name = Column(String(200), nullable=False)
    config = Column(JSON, nullable=True)
    observations = Column(JSON, nullable=True)
    metrics = Column(JSON, nullable=True)
    status = Column(String(50), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
