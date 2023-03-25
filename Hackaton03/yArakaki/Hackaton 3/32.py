lambayeque = int(input("Ingrese la población de Lambayeque: "))
lima = int(input("Ingrese la población de Lima: "))
loreto = int(input("Ingrese la población de Loreto: "))
if lambayeque > lima and lambayeque > loreto:
    print("Lambayeque es la ciudad con más población")
elif lima > lambayeque and lima > loreto:
    print("Lima es la ciudad con mas poblacion")
else: print("Loreto es la ciudad con mas poblacion")
