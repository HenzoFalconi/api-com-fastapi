from fastapi import APIRouter, HTTPException
from models.models import Motivo_Assistir
import os

router = APIRouter(prefix="/motivos_assistir")
DATA_FILE = "motivos_assistir.txt"

def ler():
    if not os.path.exists(DATA_FILE): return []
    with open(DATA_FILE) as f: return [l.strip().split("|") for l in f]

def salvar(linhas):
    with open(DATA_FILE, "w") as f: f.writelines(["|".join(l)+"\n" for l in linhas])

@router.get("/")
def listar():
    return [{"id": int(l[0]), "id_serie": int(l[1]), "motivo": l[2]} for l in ler()]

@router.post("/")
def criar(m: Motivo_Assistir):
    linhas = ler()
    for l in linhas:
        if int(l[0]) == m.id:
            raise HTTPException(400, "ID já existe")
    linhas.append([str(m.id), str(m.id_serie), m.motivo])
    salvar(linhas)
    return {"mensagem": "Criado com sucesso"}

@router.put("/")
def atualizar(m: Motivo_Assistir):
    linhas = ler()
    for i, l in enumerate(linhas):
        if int(l[0]) == m.id:
            linhas[i] = [str(m.id), str(m.id_serie), m.motivo]
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
