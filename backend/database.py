from sqlalchemy import create_engine
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)

try:
    connection = engine.connect()
    print("Banco conectado com sucesso!")
    connection.close()

except Exception as e:
    print("Erro ao conectar:")
    print(e)