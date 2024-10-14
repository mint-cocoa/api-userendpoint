# models/user.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_manager = Column(Boolean, default=False)
    park_id = Column(Integer, ForeignKey('parks.id'), nullable=True)

    # Park과의 관계 설정
    park = relationship("Park", back_populates="managers")