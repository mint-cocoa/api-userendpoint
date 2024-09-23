from pydantic import BaseModel

class ParkBase(BaseModel):
    name: str
    location: str

class ParkCreate(ParkBase):
    pass

class Park(ParkBase):
    id: int

    class Config:
        orm_mode = True
