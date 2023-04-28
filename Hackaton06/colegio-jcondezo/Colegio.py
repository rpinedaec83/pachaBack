class Alumno:
    def __init__(self,codAlum, nombre, identificador, edad, correo):
        self.codAlum = codAlum
        self.nombre = nombre
        self.identificador = identificador
        self.edad = edad
        self.correo = correo

class Curso:
    def __init__(self,codCurso, nombre):
        self.codCurso = codCurso
        self.nombre = nombre

class Profesor:
    def __init__(self,codProf, nombre, identificador, edad, correo):
        self.codProf = codProf
        self.nombre = nombre
        self.identificador = identificador
        self.edad = edad
        self.correo = correo

class cursoProfes:
    def __init__(self,codigo, codCurso, codProf):
        self.codigo = codigo
        self.codCurso = codCurso
        self.codProf = codProf

class Periodo:
    def __init__(self,codPeriodo, nombre, Anio, Mes):
        self.codPeriodo = codPeriodo
        self.nombre = nombre
        self.Anio = Anio
        self.Mes = Mes

class Salon:
    def __init__(self,codSalon, codPeriodo, codigo):
        self.codSalon = codSalon
        self.codPeriodo = codPeriodo
        self.codigo = codigo

class Notas:
    def __init__(self, codAlum, Nota1, Nota2, Nota3, Nota4, Nota5, Nota6):
        self.codAlum = codAlum
        self.Nota1 = Nota1
        self.Nota2 = Nota2
        self.Nota3 = Nota3
        self.Nota4 = Nota4
        self.Nota5 = Nota5
        self.Nota6 = Nota6
