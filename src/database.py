import os
import psycopg
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

load_dotenv()


def get_connection():

    connection = psycopg.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    return connection


def get_engine():
    connection_url = URL.create(
        drivername="postgresql+psycopg",
        username="postgres",
        password="Deeksha@123",
        host="localhost",
        port=5432,
        database="retail_db"
    )

    engine = create_engine(connection_url)

    return engine

