# Importar librerias
import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine, text   # text para la prueba de conexión
from sqlalchemy.orm import sessionmaker

# Loacalizar el archivo .env que contiene la contraseña
load_dotenv(find_dotenv())

# Extrae el valor de la contraseña
DATABASE_PASSWORD = os.getenv("DB_PASSWORD")

# Validar la carga de la variable de entorno (contraseña)
if not DATABASE_PASSWORD:
    print("Error: No se pudo leer la contraseña del archivo .env")
    exit()   # Detenemos la ejecución si no hay contraseña

# Localización completa de la Base de Datos (forzando 127.0.0.1)
DATABASE_URL = f"mysql+pymysql://root:{DATABASE_PASSWORD}@127.0.0.1:3306/GameDB"

# Carga el motor para conectarse a la base de datos
engine = create_engine(DATABASE_URL)

# Validar la conexion REAL a la DB
try:
    # Fuerza una operación mínima para comprobar que el motor y la clave funcionan.
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))   # Es como hacer "ping" a la DB
    print("\nConexión establecida con éxito a la base de datos")
except Exception as e:
    print(f"\nError: No se pudo establecer la conexión. Detalle: {e}")

# Crear la fábrica de sesiones (preparada para operar después)
Session = sessionmaker(bind=engine)