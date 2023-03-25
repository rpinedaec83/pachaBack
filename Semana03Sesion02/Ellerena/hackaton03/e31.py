suma_pares = 0
num_pares = 0
suma_impares = 0
num_impares = 0

for i in range(10):
    num = int(input("Ingrese un número: "))
if num % 2 == 0:
    suma_pares += num
    num_pares += 1
else:
    suma_impares += num
    num_impares += 1

if num_pares > 0:
    media_pares = suma_pares / num_pares
    print("La media de los números pares es:", media_pares)
else:
    print("No se ingresaron números pares.")

if num_impares > 0:
    media_impares = suma_impares / num_impares
    print("La media de los números impares es:", media_impares)
else:
    print("No se ingresaron números impares.")