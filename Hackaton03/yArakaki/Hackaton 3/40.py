n = int(input("Ingrese el número de términos para aproximar pi: "))

pi = 3
denominador = 2
signo = 1
for i in range(n):
    termino = 4/(denominador*(denominador+1)*(denominador+2))
    pi += signo*termino
    denominador += 2
    signo *= -1

print("La aproximación de pi con", n, "términos es:", pi)
