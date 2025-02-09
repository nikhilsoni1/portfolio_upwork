import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from db.models import Base

# Load DATABASE_URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# Create an engine
engine = create_engine(DATABASE_URL, echo=False)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


# Function to initialize the database
def init_db():
    Base.metadata.create_all(bind=engine)
