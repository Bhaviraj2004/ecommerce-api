from fastapi import APIRouter, Query
from typing import List
from app.models.order import OrderIn, OrderOut
from app.database.connection import db

router = APIRouter()

@router.post("/orders", response_model=OrderOut, status_code=201)
async def create_order(order: OrderIn):
    doc = order.dict()
    result = await db.orders.insert_one(doc)
    saved = await db.orders.find_one({"_id": result.inserted_id})
    saved["_id"] = str(saved["_id"])
    return saved

@router.get("/orders/{user_id}", response_model=List[OrderOut])
async def get_orders_for_user(user_id: str, limit: int = 10, offset: int = 0):
    cursor = db.orders.find({"user_id": user_id}).skip(offset).limit(limit)
    orders = []
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        orders.append(doc)
    return orders
