from psycopg2 import connect

host = "127.0.0.1"
port = 5432
dbname = "prueba"
user = "postgres"
password = "root0709"

def cadenaConexion():
    conexion = connect(host = host, port = port, dbname = dbname, user = user, password = password)

    return conexion