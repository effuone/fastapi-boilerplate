from sqlalchemy import Column, Integer, String
from src.database import metadata

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=metadata)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Integer)
