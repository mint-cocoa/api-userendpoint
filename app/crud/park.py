from sqlalchemy.orm import Session
from ..models import Park
from ..schemas import ParkCreate

def get_parks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Park).offset(skip).limit(limit).all()

def get_park(db: Session, park_id: int):
    return db.query(Park).filter(Park.id == park_id).first()

def create_park(db: Session, park: ParkCreate):
    db_park = Park(name=park.name, location=park.location)
    db.add(db_park)
    db.commit()
    db.refresh(db_park)
    return db_park
