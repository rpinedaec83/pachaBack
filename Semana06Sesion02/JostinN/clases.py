class Alumno:
    def __init__(self, nombre_alumno, edad_alumno, correo_alumno, notas_alumno, id_salon):
        self.nombre = nombre_alumno
        self.edad = edad_alumno
        self.correo = correo_alumno
        self.notas = notas_alumno
        self.id_salon = id_salon

class Salon:
    def __init__(self, nombre_salon, anio_salon):
        self.nombre = nombre_salon
        self.anio = anio_salon
        
class Profesor:
    def __init__(self, nombre_profe, edad_profe, correo_profe,id_salon):
        self.nombre = nombre_profe
        self.edad = edad_profe
        self.correo = correo_profe
        self.id_salon = id_salon

class Curso:
    def __init__(self, nombre_curso, id_profesor):
        self.nombre = nombre_curso
        self.id_profesor = id_profesor
