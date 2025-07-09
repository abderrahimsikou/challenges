from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, DateTime, Float
from dotenv import load_dotenv
import os
from datetime import datetime
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

with engine.begin() as conn:
    
    conn.execute(clients.insert(), [
        {"first_name": "Ali", "last_name": "Kamal", "email": "ali@example.com", "phone_number": "0600000001"},
        {"first_name": "Sara", "last_name": "Youssef", "email": "sara@example.com", "phone_number": "0600000002"},
        {"first_name": "Mohamed", "last_name": "Tariq", "email": "mohamed@example.com", "phone_number": "0600000003"},
        {"first_name": "Leila", "last_name": "Amine", "email": "leila@example.com", "phone_number": "0600000004"},
        {"first_name": "Omar", "last_name": "Nabil", "email": "omar@example.com", "phone_number": "0600000005"},
    ])

    conn.execute(destinations.insert(), [
        {"name": "A", "country": "France", "price_per_person": 1200.00},
        {"name": "B", "country": "Japan", "price_per_person": 1800.50},
        {"name": "C", "country": "Egypt", "price_per_person": 700.75},
        {"name": "D", "country": "USA", "price_per_person": 1600.00},
        {"name": "E", "country": "Spain", "price_per_person": 1100.25},
    ])

    conn.execute(bookings.insert(), [
        {"client_id": 1, "booking_date": datetime(2025, 7, 1), "total_price": 2400.00},
        {"client_id": 2, "booking_date": datetime(2025, 7, 3), "total_price": 1401.50},
        {"client_id": 3, "booking_date": datetime(2025, 7, 5), "total_price": 1800.25},
    ])

    conn.execute(booking_items.insert(), [
        {"booking_id": 1, "destination_id": 1, "travelers_count": 2},
        {"booking_id": 2, "destination_id": 3, "travelers_count": 2},
        {"booking_id": 3, "destination_id": 4, "travelers_count": 1},
        {"booking_id": 3, "destination_id": 5, "travelers_count": 1},
    ])
    
    
