from sqlalchemy import Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship

from infra.db.config import Base

from infra.db.enum.color import Color
from infra.db.enum.model import Model

from utils.parse import attr_aparse


class Car(Base):
    __tablename__= 'car'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    model = Column('model', Enum(Model), nullable=False)
    color = Column('color', Enum(Color),nullable=False)

    customer = relationship("Customer")

    def __repr__(self):
        return f'<id {self.id}> <customer_id {self.customer_id}> <model {self.model}> <color {self.color}>'

    def _asdict(self):
        return {'id': self.id, 'customer_id': self.customer_id, 'model': attr_aparse(self.model), 'color': attr_aparse(self.color)}
