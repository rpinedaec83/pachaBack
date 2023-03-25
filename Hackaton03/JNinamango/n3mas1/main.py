numeroSaltos = 0
currentNumber = 0

currentNumber = input("Ingrese el numero inicial de la conjetura de Collatz: ")
try:
    currentNumber = int(currentNumber)
    
    while(currentNumber != 1):
        numeroSaltos += 1
        if(currentNumber%2==0):
            currentNumber /= 2
        else:
            currentNumber = currentNumber*3 + 1

    print(f"El numero de saltos hasta 4 -> 2 -> 1 es: {numeroSaltos} ")
except ValueError as error:
    print(error)

 