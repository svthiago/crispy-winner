from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from infra.db.config import Base

from utils.parse import attr_aparse


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)

    cars = relationship("Car", primaryjoin="and_(Customer.id==Car.customer_id)")

    def __repr__(self):
        return f'<id {self.id}> <name {self.name}>'

    def _asdict(self):
        return {'id': self.id, 'name': self.name}
