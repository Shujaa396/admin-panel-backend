from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_session
from app.models.subscription import Subscription
from app.schemas.subscription import SubscriptionCreate

router = APIRouter(prefix="/subscriptions", tags=["Subscriptions"])

@router.post("/")
def create_subscription(subscription: SubscriptionCreate, db: Session = Depends(get_session)):
    db_subscription = Subscription(**subscription.dict())
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

@router.get("/")
def get_subscriptions(db: Session = Depends(get_session)):
    return db.query(Subscription).all()
