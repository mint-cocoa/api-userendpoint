from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

class Facility(Base):
    __tablename__ = "facilities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    park_id = Column(Integer, ForeignKey("parks.id"))
