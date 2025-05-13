from fastapi import APIRouter, HTTPException
from mysql.connector import Error
from models.models import Avaliacao_Serie
from database import get_connection

router = APIRouter(prefix="/avaliacoes_series")

@router.post("/")
def criar_avaliacao_serie(avaliacao_serie: Avaliacao_Serie):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ator (id, id_serie, nota, comentario, data_avaliacao) VALUES (%s, %s, %s, %s, %s)", (avaliacao_serie.id, avaliacao_serie.id_serie, avaliacao_serie.nota, avaliacao_serie.comentario, avaliacao_serie.data_avaliacao))
        conn.commit()
        return {"id": cursor.lastrowid, "mensagem": "avaliacao_serie criado com sucesso"}
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")
    finally:
        cursor.close()
        conn.close()

@router.get("/")
def listar_avaliacoes_series():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM avaliacao_serie")
        return cursor.fetchall()
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")
    finally:
        cursor.close()
        conn.close()
