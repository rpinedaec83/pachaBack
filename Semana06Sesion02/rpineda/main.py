from psycopg2 import connect, Error

try:
    conn = connect(
        user = 'postgres', 
        password = 'toor', 
        host='127.0.0.1', 
        port = '5432', 
        database = 'postgres')
    cur = conn.cursor()
    query = 'select version();'
    cur.execute(query)
    res = cur.fetchone()
    print(res)

except(Exception, Error) as error:
    print(f"Hubo un error en la conexion {str(error)}")
finally:
    cur.close()
    conn.close()
    print(f'Se ha cerrado la conexion')
