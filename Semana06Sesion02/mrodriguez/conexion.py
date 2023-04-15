import psycopg2
from psycopg2 import Error


class conexion:
    def __init__(self):
        try:
            conn = psycopg2.connect(
                user="postgres",
                password="pSecret6#",
                host="127.0.0.1",
                port=5432,
                database="hackathon05",
            )
            return conn
        except Error as error:
            print(f"Ha ocurrido un error, {error}")
            return False
