import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

host = "localhost"
database = "postgres"
user = "postgres"
password = os.getenv("DB_PASS")
port = os.getenv("DB_PORT")

def get_db_connection():
    return psycopg2.connect(
        host=host,
        dbname=database,
        user=user,
        password=password,
        port=port
    )

