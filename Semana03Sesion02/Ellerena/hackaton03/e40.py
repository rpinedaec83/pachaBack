num_iteraciones = int(input("Ingrese el número de iteraciones para la aproximación de pi: "))


pi = 3
signo = 1
divisor = 2

for i in range(num_iteraciones):
    termino = 4/(divisor * (divisor + 1) * (divisor + 2)) * signo
pi += termino
signo = -signo
divisor += 2

print("La aproximación de pi con", num_iteraciones, "iteraciones es:", pi)