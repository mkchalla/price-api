from typing import List, Optional
from datetime import datetime

from pydantic import BaseConfig, BaseModel


class APIModel(BaseModel):
    class Config(BaseConfig):
        orm_mode = True

class Token(APIModel):
    access_token: str
    token_type: str


class TokenData(APIModel):
    username: Optional[str] = None

class TokenUser(Token):
    username: Optional[str] = None

class PriceItem(APIModel):
    price: float
    udpated: datetime
    user_id: int
    product_id: int


class User(APIModel):
    username: str
    price_items: List[PriceItem] = []


class UserInDB(User):
    hashed_password: str

class UserCreate(User):
    password: str
    email: str

class ProductBase(APIModel):
    name: str
    description: Optional[str]

class ProductInDB(ProductBase):
    image: Optional[str]


class Product(ProductBase):
    price_items: List[PriceItem] = []
