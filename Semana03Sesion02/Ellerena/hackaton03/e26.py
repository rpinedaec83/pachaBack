dividendo = int(input("Introduce el dividendo: "))
divisor = int(input("Introduce el divisor: "))

cociente = 0

while dividendo >= divisor:
    dividendo -= divisor
cociente += 1

resto = dividendo

print("El cociente es:", cociente)
print("El resto es:", resto)