n = int(input("Ingrese el número de términos para aproximar pi: "))

pi = 0
for i in range(n):
    termino = 4/((2*i)+1)
    if i % 2 == 0:
        pi += termino
    else:
        pi -= termino

print("La aproximación de pi con", n, "términos es:", pi)