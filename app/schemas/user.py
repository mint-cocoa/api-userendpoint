# schemas/user.py
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str
    is_manager: bool
class User(UserBase):
    id: int
    is_active: bool
    

    class Config:
        orm_mode = True
