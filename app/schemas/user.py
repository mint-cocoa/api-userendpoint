# schemas/user.py
from pydantic import BaseModel
from typing import Optional
from pydantic import Field

class UserBase(BaseModel):
    email: str
    is_manager: bool = False
    is_active: bool = True
    park_id: Optional[int] = None

class UserCreate(UserBase):
    password: str
    park_id: Optional[int] = Field(None, description="Required if is_manager is True")

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    email: Optional[str] = None
    is_manager: Optional[bool] = None
    is_active: Optional[bool] = None
    park_id: Optional[int] = None

    class Config:
        orm_mode = True
