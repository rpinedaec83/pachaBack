import solucion
opcion = ""
print("Ingrese la tarea a ejecutar:")
while opcion != 0:
    opcion = int(input(""))
    if opcion == 0:
        continue
    try:
        ejercicio = getattr(solucion, 'tarea_'+f"{opcion:02}")()
    except Exception as ex:
        print("No implementado")
    finally:
        print("\nIngrese la tarea a ejecutar: ")
else:
    print("Fin del programa.")


