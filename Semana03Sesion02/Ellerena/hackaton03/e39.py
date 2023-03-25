num_iteraciones = int(input("Ingrese el número de iteraciones para la aproximación de pi: "))

pi = 0
signo = 1

for i in range(1, num_iteraciones*2, 2):
    termino = 4/i * signo
pi += termino
signo = -signo

print("La aproximación de pi con", num_iteraciones, "iteraciones es:", pi)