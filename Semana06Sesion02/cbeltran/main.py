#from psycopg2 import connect, Error

#try:
#    conn = connect(
#        user = 'postgres',
#        password = 'root',
#       host ='localhost',
#        port = '5432',
#        database = 'DBTIENDA'
#    )
#    cur = conn.cursor()
#    query = 'SELECT version()'
#    cur.execute(query)
#    res = cur.fetchone()
#    print(res)
#except (Exception, Error) as error:
#    print(f'Error en la conexión {str(error)}')

#finally:
#    cur.close()
#    conn.close()
#    print(f'Conexión finalizada')

from conexion import conexion
from tabulate import TableFormat, tabulate

conexion = conexion()
query = "Select * from clientes;"
datos = conexion.consultarBDD(query)
header = ['ID','Nombre','IdSegmento','IdPais','IdCiudad', 'IdEstado', 'Codigo postal', 'IdRegion']
print(tabulate(datos, headers=header, tablefmt='fancy_grid'))

nombre = input("Dime tu nombre: ")
idSegmento = int(input("ID segmento: "))
idPais = int(input("ID pais: "))
idCiudad = int(input("ID ciudad: "))
idEstado = int(input("ID estado: "))
codigoPostal =input("Código postal: ")
idRegion = int(input("ID region: "))

query=f'''insert into clientes(nombreCliente,idsegmento,idpais,idciudad,idestado,codigopostal,idregion)
values('{nombre}','{idSegmento}','{idPais}','{idCiudad}','{idEstado}','{codigoPostal}','{idRegion}');'''
print(query)
if(conexion.ejecutarBDD(query)):
    print("Datos guardados correctamente")