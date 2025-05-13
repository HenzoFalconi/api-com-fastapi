from fastapi import APIRouter, HTTPException
from mysql.connector import Error
from models.models import Ator
from database import get_connection

router = APIRouter(prefix="/atores")

@router.post("/")
def criar_ator(ator: Ator):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ator (id, nome) VALUES (%s, %s)", (ator.id, ator.nome))
        conn.commit()
        return {"id": cursor.lastrowid, "mensagem": "Ator criado com sucesso"}
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")
    finally:
        cursor.close()
        conn.close()

@router.get("/")
def listar_atores():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ator")
        return cursor.fetchall()
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")
    finally:
        cursor.close()
        conn.close()

@router.put("/")
def atualizar_ator(ator: Ator):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE ator SET nome = %s WHERE id = %s", (ator.nome, ator.id))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Ator não encontrado")
        return {"mensagem": "Ator atualizado com sucesso"}
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")
    finally:
        cursor.close()
        conn.close()

@router.delete("/")
def deletar_ator(id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ator WHERE id = %s", (id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Ator não encontrado")
        return {"mensagem": "Ator deletado com sucesso"}
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")
    finally:
        cursor.close()
        conn.close()