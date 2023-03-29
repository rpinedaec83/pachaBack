
n = int(input("Teclee un número entero positivo : "))
count = 0 # contador de saltos
while n != 1:
        print(n) # muestra el número actual
        count += 1 # incrementa el contador de saltos
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
print(n) # muestra el número 1
print("Se necesitaron", count, "saltos para llegar a 1.")