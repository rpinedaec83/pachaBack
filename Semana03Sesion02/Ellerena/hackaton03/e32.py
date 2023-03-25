provincias = ["Lambayeque", "Lima", "Loreto"]
ciudades = [[500000, 600000, 700000], [800000, 900000, 1000000], [1100000, 1200000, 1300000]]

poblacion_max = 0
ciudad_max = ""

for i in range(len(provincias)):
    for j in range(len(ciudades[i])):
        if ciudades[i][j] > poblacion_max:
            poblacion_max = ciudades[i][j]
ciudad_max = "Ciudad " + str(j+1) + " de " + provincias[i]

print("La ciudad con la población más grande es:", ciudad_max)