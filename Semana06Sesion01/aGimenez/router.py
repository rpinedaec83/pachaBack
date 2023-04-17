from database import cadenaConexion

def obtenerUsuario():
    conn = cadenaConexion()
    cursor = conn.cursor()
    sqlQuery = "select * from usuario"
    cursor.execute(sqlQuery)
    result = cursor.fetchall()

    print("este es nuestro cursor", cursor.description)
    columnas = [columna[0] for columna in cursor.description]
    resultado = [dict(zip(columnas, fila)) for fila in result]
    print("Resultado: ", resultado)
    return resultado

def eliminaUsuario(id):
    conn = cadenaConexion()
    cursor = conn.cursor()
    sqlQuery = "delete from usuario where idUsuario = %s"
    cursor.execute(sqlQuery, (id, ))
    conn.commit()
    return "Eliminado Correctamente"