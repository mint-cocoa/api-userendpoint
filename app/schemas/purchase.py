# schemas/purchase.py
from pydantic import BaseModel
from datetime import datetime

class PurchaseBase(BaseModel):
    ticket_id: int
    quantity: int

class PurchaseCreate(PurchaseBase):
    pass

class Purchase(PurchaseBase):
    id: int
    user_id: int
    purchase_date: datetime

    class Config:
        orm_mode = True
