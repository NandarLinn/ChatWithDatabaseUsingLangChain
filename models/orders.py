from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from db import Base


class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity_ordered = Column(String)
    price_each = Column(Integer)
    order_date = Column(DateTime)
    purchase_address = Column(String)
