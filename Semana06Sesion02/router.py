from database import cadena_conexion

def probar():
    conn= cadena_conexion()
    cursor = conn.cursor()
    sql_query = "select 1 + 1"
    cursor.execute(sql_query)
    result = cursor.fetchone()
    return result 