# schemas/facility.py
from pydantic import BaseModel

class FacilityBase(BaseModel):
    name: str
    description: str
    capacity: int  # 최대 수용 인원 추가

class FacilityCreate(FacilityBase):
    # park_id 필드를 제거하여 수동 입력을 방지
    pass

class Facility(FacilityBase):
    id: int
    park_id: int

    class Config:
        orm_mode = True