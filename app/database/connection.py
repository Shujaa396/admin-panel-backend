from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)

# Session generator
def get_session():
    with Session(engine) as session:
        yield session

# Create all tables on startup
def create_db_and_tables():
    from app.models import user, profile, subscription, pos_module
    SQLModel.metadata.create_all(engine)

print("✅ Connecting to DB with:", DATABASE_URL)
