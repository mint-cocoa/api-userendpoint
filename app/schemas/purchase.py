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
    qr_code: str  # QR 코드 이미지의 Base64 인코딩된 문자열

    class Config:
        orm_mode = True