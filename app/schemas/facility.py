from pydantic import BaseModel

class FacilityBase(BaseModel):
    name: str
    description: str
    capacity: int
    is_open: bool

class FacilityCreate(FacilityBase):
    pass

class Facility(FacilityBase):
    id: int
    park_id: int

    class Config:
        orm_mode = True

class FacilityStatusUpdate(FacilityBase):
    is_open: bool