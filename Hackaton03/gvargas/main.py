import solution

while True:
    opcion = int(input("Escoja el ejercicio a revisar: para terminar ponga 999"))
    if opcion == 1:
        solution.ejercicio01()
    elif opcion == 2:
        solution.ejercicio02()
    elif opcion == 999:
        print("gracias por usar el programa")
        break
    else:
        print("No implementado")
