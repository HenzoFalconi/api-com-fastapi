from fastapi import APIRouter, HTTPException
from models.models import Ator_Serie
import os

router = APIRouter(prefix="/atores_series")
DATA_FILE = "atores_series.txt"

def ler():
    if not os.path.exists(DATA_FILE): return []
    with open(DATA_FILE) as f: return [l.strip().split("|") for l in f]

def salvar(linhas):
    with open(DATA_FILE, "w") as f: f.writelines(["|".join(l)+"\n" for l in linhas])

@router.get("/")
def listar():
    return [{"id_ator": int(l[0]), "id_serie": int(l[1])} for l in ler()]

@router.post("/")
def criar(a: Ator_Serie):
    linhas = ler()
    if [str(a.id_ator), str(a.id_serie)] in linhas:
        raise HTTPException(400, "Relação já existe")
    linhas.append([str(a.id_ator), str(a.id_serie)])
    salvar(linhas)
    return {"mensagem": "Criado com sucesso"}

@router.put("/")
def atualizar(a: Ator_Serie):
    linhas = ler()
    for i, l in enumerate(linhas):
        if int(l[0]) == a.id:
            linhas[i] = [str(a.id), a.nome]
            salvar(linhas)
            return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(404, "Não encontrado")


@router.delete("/")
def deletar(id_ator: int, id_serie: int):
    linhas = ler()
    novas = [l for l in linhas if not (int(l[0]) == id_ator and int(l[1]) == id_serie)]
    if len(novas) == len(linhas): raise HTTPException(404, "Relação não encontrada")
    salvar(novas)
    return {"mensagem": "Deletado com sucesso"}

