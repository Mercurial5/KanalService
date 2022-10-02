from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import DATE

from models import Base


# Type of costs is Integers, because all the values in sheets
# are integers, and it's more comfortable to work with
class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    cost_usd = Column(Integer)
    cost_rub = Column(Integer)
    date = Column(DATE)

    def serialize(self):
        return {
            'id': self.id,
            'cost_usd': self.cost_usd,
            'cost_rub': self.cost_rub,
            'date': self.date
        }
