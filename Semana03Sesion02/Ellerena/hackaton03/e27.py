suma = 0
numeros = 0

while True:
    numero = float(input("Introduce un número positivo (introduce un negativo para acabar): "))
    if numero < 0:
        suma += numero
        numeros += 1

    if numeros > 0:
        media = suma / numeros
        print("La media es:", media)
    else:
        print("No se introdujo ningún número positivo.")

