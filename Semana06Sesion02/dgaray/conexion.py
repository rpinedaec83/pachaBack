import psycopg2
from psycopg2 import Error

class conexion:
    def conexion(self):
        try:
            conn = psycopg2.connect(user = 'postgres', 
                                    password = '021087Mikeyla', 
                                    host='127.0.0.1', 
                                    port = '5433', 
                                    database = 'postgres')
        except: