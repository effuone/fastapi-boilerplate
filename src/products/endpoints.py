from fastapi import APIRouter, HTTPException
from .crud import get_product, create_product
from .schemas import Product, ProductCreate

router = APIRouter()

@router.post("/products/", response_model=Product)
async def create_product_endpoint(product: ProductCreate):
    created_product = await create_product(product)
    if not created_product:
        raise HTTPException(status_code=400, detail="Product creation failed")
    return created_product

@router.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: int):
    db_product = await get_product(product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
