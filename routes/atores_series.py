from fastapi import APIRouter, HTTPException
from mysql.connector import Error
from models.models import Ator_Serie
from database import get_connection

router = APIRouter(prefix="/atores_series")

@router.post("/")
def criar_ator_serie(ator_serie: Ator_Serie):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ator (id_ator,id_serie, personagem) VALUES (%s, %s, %s)", (ator_serie.id_ator, ator_serie.id_serie, ator_serie.personagem))
        conn.commit()
        return {"id": cursor.lastrowid, "mensagem": "Ator_serie criado com sucesso"}
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")
    finally:
        cursor.close()
        conn.close()

@router.get("/")
def listar_atores_series():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ator_serie")
        return cursor.fetchall()
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")
    finally:
        cursor.close()
        conn.close()
