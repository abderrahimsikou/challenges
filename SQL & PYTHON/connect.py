from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import urllib.parse
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

password_encoded = urllib.parse.quote_plus(DB_PASSWORD)

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{password_encoded}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        version = result.scalar()
        print("Connexion réussie !")
        print("Version PostgreSQL :", version)
except Exception as e:
    print("Erreur de connexion :", e)