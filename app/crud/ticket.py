from sqlalchemy.orm import Session
from app.models import Ticket
from app.schemas import TicketCreate
from fastapi import APIRouter
router = APIRouter(
    prefix="/tickets",
    tags=["tickets"],
)

def create_ticket(db: Session, ticket: TicketCreate, park_id: int):
    db_ticket = Ticket(**ticket.dict(), park_id=park_id)
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def get_tickets(db: Session, park_id: int):
    return db.query(Ticket).filter(Ticket.park_id == park_id).all()

# crud/ticket.py
def get_ticket_by_id(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()