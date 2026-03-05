import psycopg2
from config import DB_CONFIG


def get_connection():

    connection = psycopg2.connect(
        database=DB_CONFIG["database"],
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        port=DB_CONFIG["port"]
    )

    return connection
