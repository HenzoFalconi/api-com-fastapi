from fastapi import APIRouter, HTTPException
from mysql.connector import Error
from models.models import Serie
from database import get_connection

router = APIRouter(prefix="/series")

@router.post("/")
def criar_serie(serie: Serie):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO serie (id, titulo, descricao, ano_lancamento, id_categoria) VALUES (%s, %s, %s, %s, %s)", (serie.id, serie.titulo, serie.descricao, serie.ano, serie.id_categoria))
        conn.commit()
        return {"id": cursor.lastrowid, "mensagem": "Serie criado com sucesso"}
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")
    finally:
        cursor.close()
        conn.close()

@router.get("/")
def listar_series():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM serie")
        return cursor.fetchall()
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")
    finally:
        cursor.close()
        conn.close()

@router.put("/")
def atualizar_serie(serie: Serie):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE serie SET titulo = %s, descricao = %s, ano_lancamento = %s, id_categoria = %s WHERE id = %s", (serie.titulo, serie.descricao, serie.ano, serie.id_categoria, serie.id))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Serie não encontrado")
        return {"mensagem": "Serie atualizado com sucesso"}
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")
    finally:
        cursor.close()
        conn.close()

@router.delete("/")
def deletar_serie(id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM serie WHERE id = %s", (id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Serie não encontrado")
        return {"mensagem": "Serie deletado com sucesso"}
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")
    finally:
        cursor.close()
        conn.close()