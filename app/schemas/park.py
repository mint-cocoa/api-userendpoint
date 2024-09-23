# schemas/park.py
from pydantic import BaseModel
from typing import List

class ParkBase(BaseModel):
    name: str
    description: str
    location: str

class ParkCreate(ParkBase):
    pass

class Park(ParkBase):
    id: int
    manager_id: int

    class Config:
        orm_mode = True
