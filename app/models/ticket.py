from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    price = Column(Integer)
    park_id = Column(Integer, ForeignKey("parks.id"))
