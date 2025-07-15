from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_session
from app.models.profile import Profile
from app.schemas.profile import ProfileCreate

router = APIRouter(prefix="/profiles", tags=["Profiles"])

@router.post("/")
def create_profile(profile: ProfileCreate, db: Session = Depends(get_session)):
    db_profile = Profile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

@router.get("/")
def get_profiles(db: Session = Depends(get_session)):
    return db.query(Profile).all()
