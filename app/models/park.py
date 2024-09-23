from sqlalchemy import Column, Integer, String
from .database import Base

class Park(Base):
    __tablename__ = "parks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
