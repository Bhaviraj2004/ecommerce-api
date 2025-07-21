from fastapi import FastAPI
from app.routes import product, order

app = FastAPI()

app.include_router(product.router)
app.include_router(order.router)
