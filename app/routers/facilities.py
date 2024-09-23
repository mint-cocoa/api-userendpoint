from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, dependencies

router = APIRouter(
    prefix="/facilities",
    tags=["facilities"],
)

@router.post("/", response_model=schemas.Facility)
def create_facility(facility: schemas.FacilityCreate, db: Session = Depends(dependencies.get_db)):
    return crud.facility.create_facility(db=db, facility=facility)

@router.get("/{facility_id}", response_model=schemas.Facility)
def read_facility(facility_id: int, db: Session = Depends(dependencies.get_db)):
    db_facility = crud.facility.get_facility(db, facility_id=facility_id)
    if db_facility is None:
        raise HTTPException(status_code=404, detail="Facility not found")
    return db_facility
