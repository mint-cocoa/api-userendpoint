from sqlalchemy.orm import Session
from ..models import Ticket
from ..schemas import TicketCreate

def get_tickets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Ticket).offset(skip).limit(limit).all()

def get_ticket(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()

def create_ticket(db: Session, ticket: TicketCreate):
    db_ticket = Ticket(type=ticket.type, price=ticket.price, park_id=ticket.park_id)
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket
