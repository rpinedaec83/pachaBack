numeros = []

for i in range(4):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

pares = [num for num in numeros if num % 2 == 0]
print(f"Hay {len(pares)} números pares")

mayor = max(numeros)
print(f"El número mayor es {mayor}")

if numeros[2] % 2 == 0:
    segundo_cuadrado = numeros[1] ** 2
    print(f"El cuadrado del segundo número es {segundo_cuadrado}")

if numeros[0] < numeros[3]:
    media = sum(numeros) / len(numeros)
    print(f"La media de los 4 números es {media}")


if numeros[1] > numeros[2] and 50 <= numeros[2] <= 700:
    suma = sum(numeros)
    print(f"La suma de los 4 números es {suma}")
