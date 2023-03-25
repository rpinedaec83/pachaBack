import solucion

opcion = -1

while opcion != 0:
    print("MENU")
    opcion = int(input("Escoja el ejercicio: "))
    print("-------------------------------")
    getattr(solucion,f'ejercicio{opcion}')()
    print("-------------------------------")


# operaciones de desempaquetado * ,, con esto puedes mandar una lista entera como parametro dentro del getattr. GOD