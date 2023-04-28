class Persona: 
    def __init__(self, identificador,nombre,  edad, correo):
        self.identificador = identificador
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

class Alumno(Persona):
    def __init__(self, identificador,nombre,  edad, correo):
        super().__init__(identificador,nombre, edad, correo)

class Profesor(Persona):
    def __init__(self, identificador,nombre, edad, correo):
        super().__init__(identificador,nombre, edad, correo)

class Salon:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre

class NotasBimetrales:
    def __init__(self, identificador, nota,  añoEscolar, bimestre):
        self.identificador = identificador
        self.nota = nota
        self.añoEscolar = añoEscolar
        self.bimestre = bimestre

class SalonAlumno:
    def __init__(self, IdSalon, IdentAlumno):
        self.IdSalon = IdSalon
        self.IdentAlumno = IdentAlumno

class SalonProfesor:
    def __init__(self, IdSalon, IdentProfesor):
        self.IdSalon = IdSalon
        self.IdentProfesor = IdentProfesor

class CursoProfesor:
    def __init__(self, IdCurso, IdentProfesor):
        self.IdCurso = IdCurso
        self.IdentProfesor = IdentProfesor