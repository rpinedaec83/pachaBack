n = int(input("Ingrese un número: "))

fibonacci = [0, 1]

for i in range(2, n+1):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print("La serie de Fibonacci de longitud", n, "es:", fibonacci)