# models/park.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Park(Base):
    __tablename__ = 'parks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    location = Column(String)
    manager_id = Column(Integer, ForeignKey('users.id'))

    manager = relationship('User')
    facilities = relationship('Facility', back_populates='park')
    tickets = relationship('Ticket', back_populates='park')
