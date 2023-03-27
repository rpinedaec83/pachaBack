pares = []
impares = []
for i in range(10):
    numero = int(input("Ingrese un número: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
mediaPares = sum(pares) / len(pares)
mediaImpares = sum(impares) / len(impares)
print("Media de los pares:", mediaPares)
print("Media de los impares:", mediaImpares)
