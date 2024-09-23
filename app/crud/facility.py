from sqlalchemy.orm import Session
from ..models import Facility
from ..schemas import FacilityCreate

def get_facilities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Facility).offset(skip).limit(limit).all()

def get_facility(db: Session, facility_id: int):
    return db.query(Facility).filter(Facility.id == facility_id).first()

def create_facility(db: Session, facility: FacilityCreate):
    db_facility = Facility(name=facility.name, park_id=facility.park_id)
    db.add(db_facility)
    db.commit()
    db.refresh(db_facility)
    return db_facility
