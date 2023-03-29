vueltas = 0

def esPar(numero):
   return numero%2 == 0

num = int(input("Numero: "))
while (num!=4):
    if (esPar(num)):
        num = num /2
    else:
        num = num * 3 + 1
    vueltas += 1

print (f"Cantidad de vueltas {vueltas}")
