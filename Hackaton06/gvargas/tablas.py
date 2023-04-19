class Salones:
    def __init__(self, Nombre, Año):
        self.Nombre = Nombre
        self.Año = Año

class Persona:
    def __init__(self,Id, Nombre, Edad, Correo, Salon ):
        self.Id = Id
        self.Nombre = Nombre
        self.Edad = Edad
        self.Correo = Correo
        self.Salon = Salon

class Alumnos(Persona):
    def __init__(self,IdAlumno, Nombre, Edad, Correo, Salon,Notas ):
        super().__init__(IdAlumno, Nombre, Edad, Correo, Salon)
        self.Notas = Notas

class Profesores(Persona):
    def __init__(self,IdProfesor, Nombre, Edad, Correo, Salon):
        super().__init__(IdProfesor, Nombre, Edad, Correo, Salon)

class Cursos:
    def __init__(self, Nombre, Profesor):
        self.Nombre = Nombre
        self.Profesor = Profesor
