from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/auth")
async def auth():
    return {"status": "ok", "token": "fake-token"}

@app.get("/orders")
async def orders():
    return {"orders": ["order1", "order2", "order3"]}

@app.get("/orders/{order_id}")
async def read_order(order_id: int, q: Optional[str] = None):
    return {"order_id": order_id, "q": q}

@app.get("/analytics")
async def analytics():
    return {"data": {"visits": 1234, "bounce_rate": "47%"}}
