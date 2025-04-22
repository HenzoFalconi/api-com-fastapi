from fastapi import FastAPI
from routes import series

app = FastAPI()

app.include_router(series.router)
