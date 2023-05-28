import psycopg2
from clases import Alumno, Salon, Curso, Profesor, conectar_db

def menu_profesor():

    while True:
        print("Menú de Profesores")
        print("1. Agregar profesor")
        print("2. Actualizar profesor")
        print("3. Eliminar profesor")
        print("4. Buscar profesor")
        print("5. Regresar")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del profesor: ")
            identificador = input("Ingrese el identificador del profesor: ")
            edad = input("Ingrese la edad del profesor: ")
            correo = input("Ingrese el correo del profesor: ")
            profesor = Profesor(nombre, identificador, edad, correo)
            profesor.insertar()
            print("Profesor agregado con éxito.")
        elif opcion == "2":
            identificador = input("Ingrese el identificador del profesor: ")
            profesor = Profesor.seleccionar(identificador)
            if profesor is None:
                print("El profesor no existe.")
            else:
                nombre = input(f"Ingrese el nuevo nombre para {profesor.nombre}: ")
                edad = input(f"Ingrese la nueva edad para {profesor.edad}: ")
                correo = input(f"Ingrese el nuevo correo para {profesor.correo}: ")
                profesor.nombre = nombre
                profesor.edad = edad
                profesor.correo = correo
                profesor.actualizar()
                print("Profesor actualizado con éxito.")
        elif opcion == "3":
            identificador = input("Ingrese el identificador del profesor: ")
            profesor = Profesor.seleccionar(identificador)
            if profesor is None:
                print("El profesor no existe.")
            else:
                profesor.eliminar()
                print("Profesor eliminado con éxito.")
        elif opcion == "4":
            identificador = input("Ingrese el identificador del profesor: ")
            profesor = Profesor.seleccionar(identificador)
            if profesor is None:
                print("El profesor no existe.")
            else:
                print("Nombre:", profesor.nombre)
                print("Identificador:", profesor.identificador)
                print("Edad:", profesor.edad)
                print("Correo:", profesor.correo)
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

    while True:
        print("Menú de Cursos")
        print("1. Agregar curso")
        print("2. Actualizar curso")
        print("3. Eliminar curso")
        print("4. Buscar curso")
        print("5. Regresar")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del curso: ")
            profesor = input("Ingrese el nombre del profesor del curso: ")
            curso = Curso(nombre, profesor)
            curso.insertar()
        elif opcion == "2":
            nombre = input("Ingrese el nombre del curso a actualizar: ")
            profesor = input("Ingrese el nombre del profesor del curso: ")
            curso = Curso.seleccionar(nombre, profesor)
            if curso is None:
                print("No se encontró el curso")
            else:
                nuevo_profesor = input("Ingrese el nuevo profesor del curso: ")
                curso.profesor = nuevo_profesor
                curso.actualizar()
        elif opcion == "3":
            nombre = input("Ingrese el nombre del curso a eliminar: ")
            profesor = input("Ingrese el nombre del profesor del curso: ")
            curso = Curso.seleccionar(nombre, profesor)
            if curso is None:
                print("No se encontró el curso")
            else:
                curso.eliminar()
        elif opcion == "4":
            nombre = input("Ingrese el nombre del curso a buscar: ")
            profesor = input("Ingrese el nombre del profesor del curso: ")
            curso = Curso.seleccionar(nombre, profesor)
            if curso is None:
                print("No se encontró el curso")
            else:
                print("Nombre:", curso.nombre)
                print("Profesor:", curso.profesor)
        elif opcion == "5":
            break
        else:
            print("Opción inválida")


    def __init__(self, nombre, anio_escolar):
        self.nombre = nombre
        self.anio_escolar = anio_escolar

    def insertar(self):
        conexion, cursor = conectar_db()
        query = "INSERT INTO salones (nombre, anio_escolar) VALUES (%s, %s);"
        datos = (self.nombre, self.anio_escolar)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self):
        conexion, cursor = conectar_db()
        query = "UPDATE salones SET anio_escolar=%s WHERE nombre=%s;"
        datos = (self.anio_escolar, self.nombre)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self):
        conexion, cursor = conectar_db()
        query = "DELETE FROM salones WHERE nombre=%s;"
        datos = (self.nombre,)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def seleccionar(nombre):
        conexion, cursor = conectar_db()
        query = "SELECT * FROM salones WHERE nombre=%s;"
        datos = (nombre,)
        cursor.execute(query, datos)
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        if resultado is None:
            return None
        else:
            nombre, anio_escolar = resultado
            return Salon(nombre, anio_escolar)

    while True:
        print("Menú de Salones")
        print("1. Agregar salón")
        print("2. Actualizar salón")
        print("3. Eliminar salón")
        print("4. Buscar salón")
        print("5. Regresar")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del salón: ")
            anio_escolar = int(input("Ingrese el año escolar del salón: "))
            salon = Salon(nombre, anio_escolar)
            salon.insertar()
        elif opcion == "2":
            nombre = input("Ingrese el nombre del salón a actualizar: ")
            anio_escolar = int(input("Ingrese el año escolar del salón: "))
            salon = Salon.seleccionar(nombre, anio_escolar)
            if salon is None:
                print("No se encontró el salón")
            else:
                anio_escolar = int(input("Ingrese el nuevo año escolar del salón: "))
                salon.anio_escolar = anio_escolar
                salon.actualizar()
        elif opcion == "3":
            nombre = input("Ingrese el nombre del salón a eliminar: ")
            anio_escolar = int(input("Ingrese el año escolar del salón: "))
            salon = Salon.seleccionar(nombre, anio_escolar)
            if salon is None:
                print("No se encontró el salón")
            else:
                salon.eliminar()
        elif opcion == "4":
            nombre = input("Ingrese el nombre del salón a buscar: ")
            anio_escolar = int(input("Ingrese el año escolar del salón: "))
            salon = Salon.seleccionar(nombre, anio_escolar)
            if salon is None:
                print("No se encontró el salón")
            else:
                print("Nombre:", salon.nombre)
                print("Año escolar:", salon.anio_escolar)
        elif opcion == "5":
            break
        else:
            print("Opción inválida")

    while True:
        print("\nMenú de Cursos")
        print("1. Agregar curso")
        print("2. Actualizar curso")
        print("3. Eliminar curso")
        print("4. Buscar curso")
        print("5. Regresar")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del curso: ")
            profesor = input("Ingrese el identificador del profesor a cargo del curso: ")
            curso = Curso(nombre, profesor)
            curso.insertar()
            print("Curso agregado con éxito.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del curso a actualizar: ")
            profesor = input("Ingrese el identificador del nuevo profesor a cargo del curso: ")
            curso = Curso(nombre, profesor)
            curso.actualizar()
            print("Curso actualizado con éxito.")

        elif opcion == "3":
            nombre = input("Ingrese el nombre del curso a eliminar: ")
            curso = Curso(nombre, None)
            curso.eliminar()
            print("Curso eliminado con éxito.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre del curso a buscar: ")
            curso = Curso.seleccionar(nombre)
            if curso is None:
                print("El curso no existe.")
            else:
                print(f"Nombre: {curso.nombre}")
                print(f"Profesor: {curso.profesor}")

        elif opcion == "5":
            break

        else:
            print("Opción inválida. Intente de nuevo.")

def menu_curso():
    while True:
        print("Menú de Cursos")
        print("1. Agregar curso")
        print("2. Actualizar curso")
        print("3. Eliminar curso")
        print("4. Buscar curso")
        print("5. Regresar")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del curso: ")
            profesor = input("Ingrese el identificador del profesor: ")
            curso = Curso(nombre, profesor)
            curso.insertar()
            print("Curso agregado exitosamente.")
        elif opcion == "2":
            nombre = input("Ingrese el nombre del curso: ")
            profesor = input("Ingrese el identificador del profesor: ")
            curso = Curso(nombre, profesor)
            curso.actualizar()
            print("Curso actualizado exitosamente.")
        elif opcion == "3":
            nombre = input("Ingrese el nombre del curso: ")
            curso = Curso.seleccionar(nombre)
            if curso is not None:
                curso.eliminar()
                print("Curso eliminado exitosamente.")
            else:
                print("Curso no encontrado.")
        elif opcion == "4":
            nombre = input("Ingrese el nombre del curso: ")
            curso = Curso.seleccionar(nombre)
            if curso is not None:
                print("Nombre:", curso.nombre)
                print("Profesor:", curso.profesor)
            else:
                print("Curso no encontrado.")
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def menu_salon():
    while True:
        print("\nMenú de Salones")
        print("1. Agregar salón")
        print("2. Actualizar salón")
        print("3. Eliminar salón")
        print("4. Buscar salón")
        print("5. Regresar")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del salón: ")
            anio_escolar = input("Ingrese el año escolar del salón: ")
            salon = Salon(nombre, anio_escolar)
            salon.insertar()
            print("Salón agregado exitosamente.")
            
        elif opcion == "2":
            nombre = input("Ingrese el nombre del salón a actualizar: ")
            anio_escolar = input("Ingrese el nuevo año escolar del salón: ")
            salon = Salon.seleccionar(nombre)
            
            if salon is None:
                print("El salón no existe.")
            else:
                salon.anio_escolar = anio_escolar
                salon.actualizar()
                print("Salón actualizado exitosamente.")
                
        elif opcion == "3":
            nombre = input("Ingrese el nombre del salón a eliminar: ")
            salon = Salon.seleccionar(nombre)
            
            if salon is None:
                print("El salón no existe.")
            else:
                salon.eliminar()
                print("Salón eliminado exitosamente.")
                
        elif opcion == "4":
            nombre = input("Ingrese el nombre del salón: ")
            salon = Salon.seleccionar(nombre)
            
            if salon is None:
                print("El salón no existe.")
            else:
                print(f"Nombre:{salon.nombre}")
                print(f"Año escolar:{salon.anio_escolar}")
                
        elif opcion == "5":
            break
            
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_alumno():
    while True:
        print("\nMenú de Alumnos")
        print("1. Agregar alumno")
        print("2. Actualizar alumno")
        print("3. Eliminar alumno")
        print("4. Buscar alumno")
        print("5. Regresar")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del alumno: ")
            identificador = input("Ingrese el identificador del alumno: ")
            edad = input("Ingrese la edad del alumno: ")
            correo = input("Ingrese el correo del alumno: ")
            alumno = Alumno(nombre, identificador, edad, correo)
            alumno.insertar()

        elif opcion == "2":
            identificador = input("Ingrese el identificador del alumno a actualizar: ")
            alumno = Alumno.seleccionar(identificador)
            if alumno is None:
                print("Alumno no encontrado")
            else:
                nombre = input(f"Ingrese el nuevo nombre para el alumno {alumno.nombre}: ")
                edad = input(f"Ingrese la nueva edad para el alumno {alumno.nombre}: ")
                correo = input(f"Ingrese el nuevo correo para el alumno {alumno.nombre}: ")
                alumno.nombre = nombre
                alumno.edad = edad
                alumno.correo = correo
                alumno.actualizar()

        elif opcion == "3":
            identificador = input("Ingrese el identificador del alumno a eliminar: ")
            alumno = Alumno.seleccionar(identificador)
            if alumno is None:
                print("Alumno no encontrado")
            else:
                alumno.eliminar()
                print(f"Alumno {alumno.nombre} eliminado exitosamente")

        elif opcion == "4":
            identificador = input("Ingrese el identificador del alumno a buscar: ")
            alumno = Alumno.seleccionar(identificador)
            if alumno is None:
                print("Alumno no encontrado")
            else:
                print(f"Nombre: {alumno.nombre}")
                print(f"Identificador: {alumno.identificador}")
                print(f"Edad: {alumno.edad}")
                print(f"Correo: {alumno.correo}")

        elif opcion == "5":
            break

        else:
            print("Opción inválida. Intente de nuevo.")

    while True:
        print("Menú de Alumnos")
        print("1. Agregar alumno")
        print("2. Actualizar alumno")
        print("3. Eliminar alumno")
        print("4. Buscar alumno")
        print("5. Regresar")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del alumno: ")
            identificador = int(input("Ingrese el identificador del alumno: "))
            edad = int(input("Ingrese la edad del alumno: "))
            correo = input("Ingrese el correo del alumno: ")
            alumno = Alumno(nombre, identificador, edad, correo)
            alumno.insertar()
        elif opcion == "2":
            identificador = int(input("Ingrese el identificador del alumno a actualizar: "))
            alumno = Alumno.seleccionar(identificador)
            if alumno is None:
                print("No se encontró el alumno")
            else:
                nombre = input("Ingrese el nombre del alumno: ")
                edad = int(input("Ingrese la edad del alumno: "))
                correo = input("Ingrese el correo del alumno: ")
                alumno.nombre = nombre
                alumno.edad = edad
                alumno.correo = correo
                alumno.actualizar()
        elif opcion == "3":
            identificador = int(input("Ingrese el identificador del alumno a eliminar: "))
            alumno = Alumno.seleccionar(identificador)
            if alumno is None:
                print("No se encontró el alumno")
            else:
                alumno.eliminar()
        elif opcion == "4":
            identificador = int(input("Ingrese el identificador del alumno a buscar: "))
            alumno = Alumno.seleccionar(identificador)
            if alumno is None:
                print("No se encontró el alumno")
            else:
                print("Nombre:", alumno.nombre)
                print("Identificador:", alumno.identificador)
                print("Edad:", alumno.edad)
                print("Correo:", alumno.correo)
        elif opcion == "5":
            break
        else:
            print("Opción inválida")

def main():
    while True:
        print("Menú principal")
        print("1. Profesores")
        print("2. Cursos")
        print("3. Salones")
        print("4. Alumnos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_profesor()
        elif opcion == "2":
            menu_curso()
        elif opcion == "3":
            menu_salon()
        elif opcion == "4":
            menu_alumno()
        elif opcion == "5":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()