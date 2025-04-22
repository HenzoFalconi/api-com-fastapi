from fastapi import APIRouter, Form, HTTPException
from mysql.connector import Error
from database import get_connection

router = APIRouter(prefix="/series")

@router.get("/")
def listar_series():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM serie")
        series = cursor.fetchall()

        return series

    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro inesperado: {str(e)}")

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass  # Caso a conexão nem tenha sido estabelecida


@router.post("/")
def criar_serie(
    titulo: str = Form(...),
    descricao: str = Form(...),
    ano: int = Form(...),
    id_categoria: int = Form(...)
):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO serie (titulo, descricao, ano_lancamento, id_categoria) VALUES (%s, %s, %s, %s)",
            (titulo, descricao, ano, id_categoria)
        )
        conn.commit()
        novo_id = cursor.lastrowid

        return {"id": novo_id, "mensagem": "Série criada com sucesso"}

    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro inesperado: {str(e)}")

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass
