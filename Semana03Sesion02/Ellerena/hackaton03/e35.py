numeros = []
for i in range(20):
    num = int(input("Ingrese un número: "))
    numeros.append(num)

    num_mayor = max(numeros)
    num_menor = min(numeros)

print("El número mayor es:", num_mayor)
print("El número menor es:", num_menor)