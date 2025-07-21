from pydantic import BaseModel, Field
from typing import List

class OrderIn(BaseModel):
    user_id: str
    product_ids: List[str]

class OrderOut(OrderIn):
    id: str = Field(alias="_id")
