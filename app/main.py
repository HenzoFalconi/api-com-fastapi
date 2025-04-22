from typing import Union 
from fastapi import FastAPI
from routes import series

app = FastAPI()

app.include_router(series.router)

@app.get("")
def read_hello():
    return {"Hello": "World"}

@app.get("/items/{item_id}?query-{query]}")
def read_item(item_id: int, query: Union[str, None] = None):
    return {"item_id": item_id, "query": query}