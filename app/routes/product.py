from fastapi import APIRouter, Query
from typing import List, Optional
from app.models.product import ProductIn, ProductOut
from app.database.connection import db

router = APIRouter()

@router.post("/products", response_model=ProductOut, status_code=201)
async def create_product(product: ProductIn):
    doc = product.dict()
    result = await db.products.insert_one(doc)
    saved = await db.products.find_one({"_id": result.inserted_id})
    saved["_id"] = str(saved["_id"])
    return saved

@router.get("/products", response_model=List[ProductOut])
async def list_products(
    name: Optional[str] = Query(None), 
    size: Optional[str] = Query(None), 
    limit: int = 10, 
    offset: int = 0
):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["size"] = size

    cursor = db.products.find(query).skip(offset).limit(limit)
    products = []
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        products.append(doc)
    return products
