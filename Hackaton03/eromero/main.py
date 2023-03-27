import funciones

print("Bienvenido a la tarea de la Hackaton")
print("Introduzca el numero del problema que desea resolver (1-40):")
while True:
    try:
        problema = int(input())
        if problema in range(1, 41):
            break
        else:
            print("Introduzca un numero valido")
    except ValueError:
        print("Introduzca un numero valido")

print("Ejecutando funcion...")
funcion = getattr(funciones, f"funcion{problema}") # Usamos getattr para obtener el nombre de la funcion del archivo funciones.py
funcion()