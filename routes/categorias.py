from fastapi import APIRouter, HTTPException
from mysql.connector import Error
from models.models import Categoria
from database import get_connection

router = APIRouter(prefix="/categorias")

@router.post("/")
def criar_categoria(categoria: Categoria):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ator (id, nome) VALUES (%s, %s)", (categoria.id, categoria.nome))
        conn.commit()
        return {"id": cursor.lastrowid, "mensagem": "Categoria criado com sucesso"}
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")
    finally:
        cursor.close()
        conn.close()

@router.get("/")
def listar_categorias():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM categoria")
        return cursor.fetchall()
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")
    finally:
        cursor.close()
        conn.close()

router.put("/")
def atualizar_categoria(categoria: Categoria):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE categoria SET nome = %s WHERE id = %s", (categoria.nome, categoria.id))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Categoria não encontrado")
        return {"mensagem": "Categoria atualizado com sucesso"}
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")
    finally:
        cursor.close()
        conn.close()