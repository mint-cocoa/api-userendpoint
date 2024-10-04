from sqlalchemy.orm import Session
from app.models import Park
from app.schemas import ParkCreate

def create_park(db: Session, park: ParkCreate):
    db_park = Park(name=park.name, description=park.description, location=park.location)
    db.add(db_park)
    db.commit()
    db.refresh(db_park)
    return db_park

def get_parks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Park).offset(skip).limit(limit).all()