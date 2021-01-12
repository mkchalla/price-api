from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType
from datetime import datetime

from .db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    email = Column(EmailType)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=False)

    price_items = relationship("PriceItem", back_populates="user")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    image = Column(String)

    price_items = relationship("PriceItem", back_populates="product")

class PriceItem(Base):
    __tablename__ = "price_item"

    id = Column(Integer, primary_key=True)
    updated = Column(DateTime, default=datetime.utcnow)
    price = Column(Float(precision=2))
    product_id = Column(Integer, ForeignKey("products.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    product = relationship("Product", back_populates="price_items")
    user = relationship("User", back_populates="price_items")
