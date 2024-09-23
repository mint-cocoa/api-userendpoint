# routers/tickets.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud, models, dependencies 

router = APIRouter(
    prefix="/tickets",
    tags=["tickets"],
)

@router.post("/{park_id}/", response_model=schemas.Ticket)
def create_ticket_for_park(park_id: int, ticket: schemas.TicketCreate, db: Session = Depends(dependencies.get_db), current_manager: models.User = Depends(dependencies.get_current_manager)):
    # 권한 확인 로직 추가 필요
    return crud.ticket.create_ticket(db=db, ticket=ticket, park_id=park_id)

@router.get("/{park_id}/", response_model=List[schemas.Ticket])
def read_tickets_for_park(park_id: int, db: Session = Depends(dependencies.get_db)):
    tickets = crud.ticket.get_tickets(db, park_id=park_id)
    return tickets  
