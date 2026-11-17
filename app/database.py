
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Read database connection from environment variables.
# Fall back to SQLite for local development.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./auto_dealer.db"
)

# SQLite requires this setting when used with FastAPI.
connect_args = {}

if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

# Create SQLAlchemy engine.
engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    pool_pre_ping=True
)

# Create database sessions.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for database models.
Base = declarative_base()


# Database dependency for FastAPI endpoints.
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
