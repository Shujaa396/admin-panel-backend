from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_session
from app.models.pos_module import POSModule
from app.schemas.pos_module import POSModuleCreate

router = APIRouter(prefix="/pos-modules", tags=["POS Modules"])

@router.post("/")
def create_pos_module(module: POSModuleCreate, db: Session = Depends(get_session)):
    db_module = POSModule(**module.dict())
    db.add(db_module)
    db.commit()
    db.refresh(db_module)
    return db_module

@router.get("/")
def get_pos_modules(db: Session = Depends(get_session)):
    return db.query(POSModule).all()
