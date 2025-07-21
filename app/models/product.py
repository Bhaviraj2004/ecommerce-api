from pydantic import BaseModel, Field

class ProductIn(BaseModel):
    name: str
    size: str
    price: float

class ProductOut(ProductIn):
    id: str = Field(alias="_id")
