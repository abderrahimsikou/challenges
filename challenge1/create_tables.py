from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, DateTime, Float
from dotenv import load_dotenv
import os
import urllib.parse

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
data = MetaData()

clients = Table(
    'clients', data,
    Column('client_id', Integer, primary_key=True, autoincrement=True),
    Column('first_name', String(100)),
    Column('last_name', String(100)),
    Column('email', String(150)),
    Column('phone_number', String(50))
)

destinations = Table(
    'destinations', data,
    Column('destination_id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(100)),
    Column('country', String(100)),
    Column('price_per_person', Float)
)

bookings = Table(
    'bookings', data,
    Column('booking_id', Integer, primary_key=True, autoincrement=True),
    Column('client_id', Integer, ForeignKey("clients.client_id")),
    Column('booking_date', DateTime),
    Column('total_price', Float)
)

booking_items = Table(
    'booking_items', data,
    Column('item_id', Integer, primary_key=True, autoincrement=True),
    Column('booking_id', Integer, ForeignKey("bookings.booking_id")),
    Column('destination_id', Integer, ForeignKey("destinations.destination_id")),
    Column('travelers_count', Integer)
)

try:
    data.create_all(engine)
except Exception as e:
    print(e)