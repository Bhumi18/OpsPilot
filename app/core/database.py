from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import settings

# Create SQLAlchemy engine with connection pool pre-ping to ensure active connections
engine = create_engine(
    settings.sync_database_url,
    pool_pre_ping=True
)

# Request-scoped session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy ORM models."""
    pass


def get_db() -> Generator[Session, None, None]:
    """Dependency generator that yields a database session per HTTP request and closes it after completion."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
