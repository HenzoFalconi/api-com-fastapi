from fastapi import FastAPI
from routes import series, motivos_assistir, avaliacoes_series, categorias, atores, atores_series

app = FastAPI()


app.include_router(series.router, prefix="/series", tags=["Séries"])
app.include_router(motivos_assistir.router, prefix="/motivos", tags=["Motivos Assistir"])
app.include_router(avaliacoes_series.router, prefix="/avaliacoes", tags=["Avaliações"])
app.include_router(categorias.router, prefix="/categorias", tags=["Categorias"])
app.include_router(atores.router, prefix="/atores", tags=["Atores"])
app.include_router(atores_series.router, prefix="/elencos", tags=["Atores em Séries"])
