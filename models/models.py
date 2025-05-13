import datetime
from pydantic import BaseModel

class Serie(BaseModel):
    id: int
    titulo: str
    descricao: str
    ano: int
    id_categoria: int

class Categoria(BaseModel):
    id: int
    nome: str

class Ator(BaseModel):
    id: int
    nome: str

class Ator_Serie(BaseModel):
    id_serie: int
    id_ator: int
    personagem: str

class Avaliacao_Serie(BaseModel):
    id: int
    id_serie: int
    nota: int
    comentario: str
    data_avaliacao: datetime.date

class Motivo_Assistir(BaseModel):
    id: int
    id_serie: int
    motivo: str