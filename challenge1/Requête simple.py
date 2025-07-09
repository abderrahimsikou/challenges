from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, DateTime, Float, select
from dotenv import load_dotenv
import os
import urllib.parse
from create_tables import clients
from create_tables import destinations
from create_tables import bookings
from create_tables import booking_items

# Connect to DataBase
# ========================================================================
load_dotenv()

DB_HOST     = os.getenv("DB_HOST")
DB_PORT     = os.getenv("DB_PORT")
DB_USER     = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME     = os.getenv("DB_NAME")

password_encoded = urllib.parse.quote_plus(DB_PASSWORD)

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{password_encoded}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

#=========================================================================

client = select(clients.c.first_name, clients.c.email, clients.c.email, clients.c.phone_number)

with engine.connect() as conn:
    data = conn.execute(client)
    for i in data:
        print(i)
        
prix = select(destinations).where(destinations.c.price_per_person > 1000)

with engine.connect() as conn:
    data = conn.execute(prix)
    for i in data:
        print(i)