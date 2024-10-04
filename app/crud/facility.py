from sqlalchemy.orm import Session
from app.models import Facility
from app.schemas import FacilityCreate
from app.dependencies import get_current_user  # 현재 사용자 정보를 가져오는 함수
from fastapi import HTTPException

def get_facilities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Facility).offset(skip).limit(limit).all()

def get_facility(db: Session, facility_id: int):
    return db.query(Facility).filter(Facility.id == facility_id).first()

def create_facility(db: Session, facility: FacilityCreate, current_user):
    if not current_user.is_manager:
        raise HTTPException(status_code=403, detail="Only managers can create facilities")
    
    # 현재 사용자의 소속 공원 ID를 사용
    db_facility = Facility(name=facility.name, park_id=current_user.park_id)
    db.add(db_facility)
    db.commit()
    db.refresh(db_facility)
    return db_facility
