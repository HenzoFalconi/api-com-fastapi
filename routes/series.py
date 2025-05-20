from fastapi import APIRouter, HTTPException
from models.models import Serie
import os

router = APIRouter(prefix="/series")
DATA_FILE = "series.txt"

def ler_arquivo():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return [linha.strip().split("|") for linha in f.readlines()]

def salvar_arquivo(linhas):
    with open(DATA_FILE, "w") as f:
        f.writelines([f"{'|'.join(l)}\n" for l in linhas])

@router.get("/")
def listar_series():
    return [{"id": int(l[0]), "titulo": l[1], "descricao": l[2], "ano": int(l[3]), "id_categoria": int(l[4])} for l in ler_arquivo()]

@router.post("/")
def criar_serie(serie: Serie):
    linhas = ler_arquivo()
    for l in linhas:
        if int(l[0]) == serie.id:
            raise HTTPException(status_code=400, detail="ID já existe")
    linhas.append([str(serie.id), serie.titulo, serie.descricao, str(serie.ano), str(serie.id_categoria)])
    salvar_arquivo(linhas)
    return {"mensagem": "Serie criada com sucesso"}

@router.put("/")
def atualizar_serie(serie: Serie):
    linhas = ler_arquivo()
    for i, l in enumerate(linhas):
        if int(l[0]) == serie.id:
            linhas[i] = [str(serie.id), serie.titulo, serie.descricao, str(serie.ano), str(serie.id_categoria)]
            salvar_arquivo(linhas)
            return {"mensagem": "Serie atualizada com sucesso"}
    raise HTTPException(status_code=404, detail="Serie não encontrada")

@router.delete("/")
def deletar_serie(id: int):
    linhas = ler_arquivo()
    novas = [l for l in linhas if int(l[0]) != id]
    if len(linhas) == len(novas):
        raise HTTPException(status_code=404, detail="Serie não encontrada")
    salvar_arquivo(novas)
    return {"mensagem": "Serie deletada com sucesso"}
