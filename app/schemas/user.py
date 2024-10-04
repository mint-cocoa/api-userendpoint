# schemas/user.py
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    is_manager: bool
    is_active: bool = True
class UserCreate(UserBase):
    password: str
class User(UserBase):
    id: int
    class Config:
        orm_mode = True
