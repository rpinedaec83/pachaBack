def ejercicio01():
    #Hacer un programa en Python que lea un número por el teclado y determinar si tiene tres dígitos
    numero = int(input("Escribe un numero: "))
    strnumero = str(numero)
    if len(strnumero) == 3:
        print(f"Este numero tiene {len(strnumero)} digitos")
    else:
        print(f"Este numero no cumple con la condicion solo tiene {len(strnumero)} digitos")

def ejercicio02():
    #2. Hacer un programa en Python que lea un número entero por el teclado y determinar si es negativo.
    print("Es negativo o no")