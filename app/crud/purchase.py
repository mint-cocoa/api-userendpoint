from sqlalchemy.orm import Session
from ..models import Purchase
from ..schemas import PurchaseCreate

def get_purchases(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Purchase).offset(skip).limit(limit).all()

def get_purchase(db: Session, purchase_id: int):
    return db.query(Purchase).filter(Purchase.id == purchase_id).first()

def create_purchase(db: Session, purchase: PurchaseCreate):
    db_purchase = Purchase(user_id=purchase.user_id, ticket_id=purchase.ticket_id, quantity=purchase.quantity)
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase
