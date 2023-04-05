from Utils import*
def main():
    while True:
        print("\nSeleccione una opción:")
        print("1. Registrar un alumno")
        print("2. Registrar un docente")
        print("3. Salir")

        opcion = input("> ")

        if opcion == "1":
            registrar_alumno()
        elif opcion == "2":
            registrar_docente()
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()