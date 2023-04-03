from models.Models import Alumno,Docente
def registrar_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    dni = input("Ingrese el DNI del alumno: ")
    edad = input("Ingrese la edad del alumno: ")
    alumno = Alumno(nombre, dni, edad)

    notas = []
    while len(notas) < 4:
        nota = float(input("Ingrese una nota: "))
        if nota<20:
            alumno.agregar_nota(nota)
            notas.append(nota)
        else:
            print("Nota no válida.")

    promedio = alumno.promedio_notas()

    with open("alumnos.txt", "a") as archivo:
        reporte = alumno.reporte()
        archivo.write(reporte + "\n")
        print(f"Alumno registrado correctamente.\nReporte: \n{reporte}")

def registrar_docente():
    nombre = input("Ingrese el nombre del docente: ")
    dni = input("Ingrese el DNI del docente: ")
    edad = input("Ingrese la edad del docente: ")
    docente = Docente(nombre, dni, edad)

    with open("docentes.txt", "a") as archivo:
        reporte = docente.reporte()
        archivo.write(reporte + "\n")
        print(f"Docente registrado correctamente. \nReporte: \n{reporte}")