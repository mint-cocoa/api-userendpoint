from pydantic import BaseModel

class PurchaseBase(BaseModel):
    user_id: int
    ticket_id: int
    quantity: int

class PurchaseCreate(PurchaseBase):
    pass

class Purchase(PurchaseBase):
    id: int

    class Config:
        orm_mode = True
