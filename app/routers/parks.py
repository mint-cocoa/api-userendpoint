# routers/parks.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud, models, dependencies

router = APIRouter(
    prefix="/parks",
    tags=["parks"],
)

@router.post("/", response_model=schemas.Park)
def create_park(park: schemas.ParkCreate, db: Session = Depends(dependencies.get_db)):
    return crud.park.create_park(db=db, park=park)

@router.get("/", response_model=List[schemas.Park])
def read_parks(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    parks = crud.park.get_parks(db, skip=skip, limit=limit)
    return parks
