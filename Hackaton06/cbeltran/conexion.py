import psycopg2
from psycopg2 import Error

class conexion:
    def conexion(self):
        try:
            conn = psycopg2.connect(user='postgres',
                                    password="root",
                                    host="localhost",
                                    port="5432",
                                    database="sv70098291")
            return conn
        except Error as error:
            print(f"Error de conexión: {str(error)}")
            return False
        
    def ConsultarQuery(self, query): 
        try:    
            conexion = self.conexion()
            cur = conexion.cursor()
            cur.execute(query)
            records = cur.fetchall()
            return records
        except Error as error:
            print(f"Ha ocurrido un error: {str(error)}")
            return False
        finally:
            if(conexion):
                cur.close()
                conexion.close()

    def EjecutarQuery(self, query):
        try:
            conexion = self.conexion()
            cur = conexion.cursor()
            cur.execute(query)
            conexion.commit()
            exito = True
            return exito
        except Error as error:
            print(f"Ha ocurrido un error: {str(error)}")
            input("Desea Continuar")
            return False
        finally:
            if(conexion):
                cur.close()
                conexion.close()