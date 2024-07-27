from sqlalchemy import insert, select
from .models import Product
from .schemas import ProductCreate
from src.database import fetch_one, fetch_all, execute

async def get_product(product_id: int):
    query = select(Product).where(Product.id == product_id)
    return await fetch_one(query)

async def create_product(product: ProductCreate):
    query = insert(Product).values(name=product.name, description=product.description, price=product.price).returning(Product)
    return await fetch_one(query, commit_after=True)
