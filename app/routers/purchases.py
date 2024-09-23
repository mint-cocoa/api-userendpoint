# routers/purchases.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud, models, dependencies
router = APIRouter()

@router.post("/", response_model=schemas.Purchase)
def create_purchase(purchase: schemas.PurchaseCreate, db: Session = Depends(dependencies.get_db), current_user: models.User = Depends(dependencies.get_current_active_user)):
    # 실제 결제 처리 로직 추가 필요
    return crud.purchase.create_purchase(db=db, purchase=purchase, user_id=current_user.id)
