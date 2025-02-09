from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database Configuration
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/dev"

# Create SQLAlchemy Engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()

def get_db():
    """Dependency to get a new session instance."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
