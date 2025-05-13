from fastapi import APIRouter, HTTPException
from mysql.connector import Error
from models.models import Motivo_Assistir
from database import get_connection

router = APIRouter(prefix="/motivos_assistir")

@router.post("/")
def criar_motivo_assistr(motivo_assistir: Motivo_Assistir):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ator (id, nome) VALUES (%s, %s, %s)", (motivo_assistir.id, motivo_assistir.id_serie, motivo_assistir.motivo))  
        conn.commit()
        return {"id": cursor.lastrowid, "mensagem": "Motivo_Assistir criado com sucesso"}
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")
    finally:
        cursor.close()
        conn.close()

@router.get("/")
def listar_motivos_assistr():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM motivo_assistir")
        return cursor.fetchall()
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")
    finally:
        cursor.close()
        conn.close()

@router.put("/")
def atualizar_motivo_assistr(motivo_assistir: Motivo_Assistir):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE motivo_assistir SET nome = %s WHERE id = %s", (motivo_assistir.motivo, motivo_assistir.id))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Motivo_Assistir não encontrado")
        return {"mensagem": "Motivo_Assistir atualizado com sucesso"}
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")
    finally:
        cursor.close()
        conn.close()