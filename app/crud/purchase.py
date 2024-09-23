# crud/purchase.py
from sqlalchemy.orm import Session
from app.models import Purchase
from app.schemas import PurchaseCreate

def create_purchase(db: Session, purchase: PurchaseCreate, user_id: int):
    db_purchase = Purchase(**purchase.dict(), user_id=user_id)
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase
