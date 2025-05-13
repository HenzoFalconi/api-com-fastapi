from fastapi import FastAPI
from routes import series, atores, categorias, atores_series, avaliacoes_series, motivos_assistir

app = FastAPI()

app.include_router(series.router)
app.include_router(atores.router)
app.include_router(categorias.router)
app.include_router(atores_series.router)
app.include_router(avaliacoes_series.router)
app.include_router(motivos_assistir.router)