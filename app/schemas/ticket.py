from pydantic import BaseModel

class TicketBase(BaseModel):
    type: str
    price: int
    park_id: int

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    id: int

    class Config:
        orm_mode = True
