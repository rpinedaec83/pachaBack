from conexion import Conexion
from models import *
URI  = "mongodb://localhost:27017"
database = "Pachaqtec"

conn = Conexion(URI,database)

alumno = Alumno(1,"juan",15,"eljuan@hotmail.com")

conn.insertar_registro("alumnos",alumno.ToDic())