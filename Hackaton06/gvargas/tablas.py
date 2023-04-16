class Salones:
    def __init__(self, Nombre, Año):
        self.Nombre = Nombre
        self.Año = Año

class Alumnos:
    def __init__(self,IdAlumno, Nombre, Edad, Correo, Salon,Notas ):
        self.IdAlumno = IdAlumno
        self.Nombre = Nombre
        self.Edad = Edad
        self.Correo = Correo
        self.Salon = Salon
        self.Notas = Notas

class Profesores:
    def __init__(self,IdProfesor, Nombre, Edad, Correo, Salon):
        self.IdProfesor = IdProfesor
        self.Nombre = Nombre
        self.Edad = Edad
        self.Correo = Correo
        self.Salon = Salon

class Cursos:
    def __init__(self, Nombre, Profesor):
        self.Nombre = Nombre
        self.Profesor = Profesor
