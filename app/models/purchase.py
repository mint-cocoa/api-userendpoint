# models/purchase.py
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Purchase(Base):
    __tablename__ = 'purchases'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    ticket_id = Column(Integer, ForeignKey('tickets.id'))
    quantity = Column(Integer)
    purchase_date = Column(DateTime, default=datetime.utcnow)

    user = relationship('User')
    ticket = relationship('Ticket')
