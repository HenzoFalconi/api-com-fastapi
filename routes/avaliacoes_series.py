from fastapi import APIRouter, HTTPException
from models.models import Avaliacao_Serie
import os

router = APIRouter(prefix="/avaliacoes_series")
DATA_FILE = "avaliacoes_series.txt"

def ler():
    if not os.path.exists(DATA_FILE): return []
    with open(DATA_FILE) as f: return [l.strip().split("|") for l in f]

def salvar(linhas):
    with open(DATA_FILE, "w") as f: f.writelines(["|".join(l)+"\n" for l in linhas])

@router.get("/")
def listar():
    return [{"id": int(l[0]), "id_serie": int(l[1]), "nota": float(l[2]), "comentario": l[3]} for l in ler()]

@router.post("/")
def criar(a: Avaliacao_Serie):
    linhas = ler()
    for l in linhas:
        if int(l[0]) == a.id:
            raise HTTPException(400, "ID já existe")
    linhas.append([str(a.id), str(a.id_serie), str(a.nota), a.comentario])
    salvar(linhas)
    return {"mensagem": "Criado com sucesso"}

@router.put("/")
def atualizar(a: Avaliacao_Serie):
    linhas = ler()
    for i, l in enumerate(linhas):
        if int(l[0]) == a.id:
            linhas[i] = [str(a.id), str(a.id_serie), str(a.nota), a.comentario]
            salvar(linhas)
            return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(404, "Não encontrado")

@router.delete("/")
def deletar(id: int):
    linhas = ler()
    novas = [l for l in linhas if int(l[0]) != id]
    if len(linhas) == len(novas): raise HTTPException(404, "Não encontrado")
    salvar(novas)
    return {"mensagem": "Deletado com sucesso"}