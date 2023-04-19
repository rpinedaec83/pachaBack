class Alumno:
    def __init__(self, nombre, identificador, edad, correo, salon):
        self.nombre = nombre
        self.identificador = identificador
        self.edad = edad
        self.correo = correo
        self.salon = salon
        self.notas = {}

    def agregar_nota(self, curso, bimestre, nota):
        if curso not in self.notas:
            self.notas[curso] = {}
        self.notas[curso][bimestre] = nota

    def obtener_promedio(self, curso):
        notas_curso = self.notas.get(curso, {})
        if notas_curso:
            return sum(notas_curso.values()) / len(notas_curso)
        else:
            return None


class Profesor:
    def __init__(self, nombre, identificador, edad, correo):
        self.nombre = nombre
        self.identificador = identificador
        self.edad = edad
        self.correo = correo

    def cambiar_curso(self, salon, curso_actual, curso_nuevo):
        salon.cambiar_curso(self, curso_actual, curso_nuevo)


class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor

    def asignar_profesor(self, profesor):
        self.profesor = profesor


class Salon:
    def __init__(self, nombre, ano_escolar):
        self.nombre = nombre
        self.ano_escolar = ano_escolar
        self.alumnos = []
        self.cursos = {}

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def agregar_curso(self, curso):
        self.cursos[curso.nombre] = curso

    def cambiar_curso(self, profesor, curso_actual, curso_nuevo):
        if curso_actual in self.cursos and self.cursos[curso_actual].profesor == profesor:
            curso = self.cursos.pop(curso_actual)
            curso.nombre = curso_nuevo
            self.cursos[curso_nuevo] = curso
            print(f"El curso {curso_actual} ha sido renombrado a {curso_nuevo}.")

    def obtener_promedio_curso(self, curso):
        notas = []
        for alumno in self.alumnos:
            promedio = alumno.obtener_promedio(curso)
            if promedio is not None:
                notas.append(promedio)
        if notas:
            return sum(notas) / len(notas)
        else:
            return None


if __name__ == '__main__':
    salon = Salon("Salon 1", "2023")
    profesor1 = Profesor("Juan Perez", "001", 35, "juan.perez@colegio.com")
    profesor2 = Profesor("Ana Rodriguez", "002", 40, "ana.rodriguez@colegio.com")
    curso1 = Curso("Matemáticas", profesor1)
    curso2 = Curso("Ciencias", profesor2)
    salon.agregar_curso(curso1)
    salon.agregar_curso(curso2)

    alumno1 = Alumno("Maria Hernandez", "1001", 16, "maria.hernandez@colegio.com", salon)
    alumno2 = Alumno("Pedro Gomez", "1002", 17, "pedro.gomez@colegio.com", salon)
