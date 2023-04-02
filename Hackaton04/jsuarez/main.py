from archivo_alumnos import Alumno
from archivo_docentes import Docente

while True:
    print("1. Registrar docente")
    print("2. Registrar alumno")
    print("3. Generar reporte de alumnos")
    print("4. Generar reporte de docentes")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del docente: ")
        dni = input("Ingrese el DNI del docente: ")
        edad = input("Ingrese la edad del docente: ")
        docente = Docente(nombre, dni, edad)
        docente.registrar_datos()

    elif opcion == "2":
        nombre = input("Ingrese el nombre del alumno: ")
        dni = input("Ingrese el DNI del alumno: ")
        edad = input("Ingrese la edad del alumno: ")
        notas = []
        for i in range(4):
            nota = float(input(f"Ingrese la nota {i+1}: "))
            notas.append(nota)
        alumno = Alumno(nombre, dni, edad, notas)
        alumno.registrar_datos()

    elif opcion == "3":
        reporte = Alumno.generar_reporte()
        with open("reporte_alumnos.txt", "w") as archivo:
            archivo.write(reporte)

    elif opcion == "4":
        reporte = Docente.generar_reporte()
        with open("reporte_docentes.txt", "w") as archivo:
            archivo.write(reporte)

    elif opcion == "5":
        break

    else:
        print("Opción inválida. Intente nuevamente.")
