from pydantic import BaseModel

class FacilityBase(BaseModel):
    name: str
    park_id: int

class FacilityCreate(FacilityBase):
    pass

class Facility(FacilityBase):
    id: int

    class Config:
        orm_mode = True
