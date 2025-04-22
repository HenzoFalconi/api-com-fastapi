from fastapi import FastAPI
from routes import series

app = FastAPI()

# Certifique-se de que o router está sendo incluído
app.include_router(series.router)
