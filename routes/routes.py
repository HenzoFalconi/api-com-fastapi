from fastapi import APIRouter
from routes import series, motivos_assistir, avaliacoes_series, categorias, atores, atores_series

router = APIRouter(prefix="/api")

router.include_router(series.router, prefix="/series", tags=["Séries"])
router.include_router(motivos_assistir.router, prefix="/motivos", tags=["Motivos Assistir"])
router.include_router(avaliacoes_series.router, prefix="/avaliacoes", tags=["Avaliações"])
router.include_router(categorias.router, prefix="/categorias", tags=["Categorias"])
router.include_router(atores.router, prefix="/atores", tags=["Atores"])
router.include_router(atores_series.router, prefix="/elencos", tags=["Atores em Séries"])
