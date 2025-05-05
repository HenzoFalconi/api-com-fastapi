import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        print("Tentando conectar ao banco de dados...")
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            connection_timeout=5  # evita carregamento infinito
        )
        print("Conexão bem-sucedida.")
        return conn
    except mysql.connector.Error as err:
        print(f"Erro na conexão com o banco de dados: {err}")
        raise
