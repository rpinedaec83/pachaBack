def mediaPositivos():
    numeros = []
    while True:
        numero = int(input("Ingrese un número positivo (ingrese un negativo para terminar): "))
        if numero < 0:
            break
        numeros.append(numero)
    media = sum(numeros) / len(numeros)
    return media
