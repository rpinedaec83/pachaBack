numeros = []
for i in range(20):
    numeros.append(int(input("Ingrese un número: ")))
    
maximo = numeros[0]
minimo = numeros[0]

for numero in numeros:
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero

print("El número máximo es:", maximo)
print("El número mínimo es:", minimo)
