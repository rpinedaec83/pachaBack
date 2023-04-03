import pickle

class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

class Alumno(Persona):
    def __init__(self, nombre, edad, dni):
        super().__init__(nombre, edad, dni)
        self.notas = []
    
    def agregar_nota(self, nota):
        self.notas.append(nota)
    
    def promedio_notas(self):
        return sum(self.notas)/len(self.notas)

# Registrar un alumno
alumno = Alumno("Juan", 18, "12345678")
alumno.agregar_nota(15)
alumno.agregar_nota(18)
alumno.agregar_nota(16)
alumno.agregar_nota(20)

# Guardar el alumno en un archivo de texto
with open("alumnos.txt", "wb") as f:
    pickle.dump(alumno, f)

# Cargar el alumno desde el archivo de texto
with open("alumnos.txt", "rb") as f:
    alumno_cargado = pickle.load(f)

# Mostrar el promedio de las notas del alumno
print("Promedio de notas:", alumno_cargado.promedio_notas())

# Crear un reporte con el promedio de notas de todos los alumnos
with open("reporte_alumnos.txt", "w") as f:
    for i in range(1, 11):
        # Supongamos que tenemos 10 alumnos registrados
        try:
            with open(f"alumno_{i}.txt", "rb") as f_alumno:
                alumno = pickle.load(f_alumno)
                max_nota = max(alumno.notas)
                min_nota = min(alumno.notas)
                promedio = alumno.promedio_notas()
                f.write(f"nro : {i}\n")
                f.write(f"-Alumno: {alumno.nombre}, máxima nota: {max_nota}, mínima nota: {min_nota}, promedio: {promedio}\n")
        except:
            continue

# Registrar un docente
docente = Persona("Pedro", 35, "87654321")

# Guardar el docente en un archivo de texto
with open("docentes.txt", "wb") as f:
    pickle.dump(docente, f)

# Cargar el docente desde el archivo de texto
with open("docentes.txt", "rb") as f:
    docente_cargado = pickle.load(f)

# Mostrar los datos del docente
print("Nombre:", docente_cargado.nombre)
print("Edad:", docente_cargado.edad)
print("DNI:", docente_cargado.dni)
