# app/routes/user.py

from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.database.connection import get_session
from app.models.user import User
from app.schemas.user import UserCreate

router = APIRouter(prefix="/users", tags=["Users"])  # ✅ This line was missing before

@router.post("/")
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    db_user = User(**user.dict())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@router.get("/")
def get_users(session: Session = Depends(get_session)):
    return session.exec(select(User)).all()
