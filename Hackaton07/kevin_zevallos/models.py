class Alumno:
    def __init__(self,id,nombre,edad,correo):
        self.id = id
        self.nombre = nombre
        self.edad=edad
        self.correo = correo
    def ToDic(self):
        return{
            "nombre":self.nombre,
            "edad":self.edad,
            "correo":self.correo
        }

class Salon:
    def __init__(self,nombreSalon,anoEscolar):
        self.nombreSalon = nombreSalon
        self.anoEscolar = anoEscolar
    def ToDic(self):
        return{
            "nombre del salon":self.nombreSalon,
            "año escolar": self.anoEscolar
        }

class Cursos:
    def __init__(self,nombreCurso,nomnreProfesor):
        self.nombreCurso=nombreCurso
        self.nombreProfesor=nomnreProfesor
    def ToDic(self):
        return{
            "nombre del curso":self.nombreCurso,
            "profesor asignado":self.nombreProfesor
        }

class Profesor:
    def __init__(self,id,nombre,edad,correo):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
    def ToDic(self):
        return{
            "nombre":self.nombre,
            "edad":self.edad,
            "correo":self.correo
        }