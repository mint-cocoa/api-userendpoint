# schemas/ticket.py
from pydantic import BaseModel

class TicketBase(BaseModel):
    title: str
    description: str
    price: float

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    id: int
    park_id: int

    class Config:
        orm_mode = True
