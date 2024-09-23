from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, dependencies

router = APIRouter(
    prefix="/purchases",
    tags=["purchases"],
)

@router.post("/", response_model=schemas.Purchase)
def create_purchase(purchase: schemas.PurchaseCreate, db: Session = Depends(dependencies.get_db)):
    return crud.purchase.create_purchase(db=db, purchase=purchase)

@router.get("/{purchase_id}", response_model=schemas.Purchase)
def read_purchase(purchase_id: int, db: Session = Depends(dependencies.get_db)):
    db_purchase = crud.purchase.get_purchase(db, purchase_id=purchase_id)
    if db_purchase is None:
        raise HTTPException(status_code=404, detail="Purchase not found")
    return db_purchase
