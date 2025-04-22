from fastapi import APIRouter
from database import get_connection

router = APIRouter(prefix="/series")  # <- isso é importante

@router.get("/")
def listar_series():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM serie")
    series = cursor.fetchall()

    cursor.close()
    conn.close()
    return series

@router.post("/")
def criar_serie(titulo: str, descricao: str, ano: int, id_categoria: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO serie (titulo, descricao, ano_lancamento, id_categoria) VALUES (%s, %s, %s, %s)",
        (titulo, descricao, ano, id_categoria)
    )
    conn.commit()
    novo_id = cursor.lastrowid

    cursor.close()
    conn.close()
    return {"id": novo_id, "mensagem": "Série criada com sucesso"}
