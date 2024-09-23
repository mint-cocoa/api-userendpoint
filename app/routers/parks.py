from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, dependencies

router = APIRouter(
    prefix="/parks",
    tags=["parks"],
)

@router.post("/", response_model=schemas.Park)
def create_park(park: schemas.ParkCreate, db: Session = Depends(dependencies.get_db)):
    return crud.park.create_park(db=db, park=park)

@router.get("/{park_id}", response_model=schemas.Park)
def read_park(park_id: int, db: Session = Depends(dependencies.get_db)):
    db_park = crud.park.get_park(db, park_id=park_id)
    if db_park is None:
        raise HTTPException(status_code=404, detail="Park not found")
    return db_park
