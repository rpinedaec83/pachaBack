
#Algoritmo Conjetura de Collatz, muestra los numeros  por los que se pasa antes de entrar al bucle

num = int(input("Ingresa un numero diferente de 1: "))
pasos = 0

while num != 1:
    pasos += 1
    if num % 2 == 0:
        num = num / 2
    else:
        num = num * 3 + 1
    print(int(num))    
    continue

print(f"Numero de pasos antes del reinicio: {pasos}")