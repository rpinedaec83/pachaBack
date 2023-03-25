precio_helado = 100
tipo_membresia = input("Ingrese su tipo de membresía (A, B o C): ")

if tipo_membresia == "A":
    descuento = 0.1
elif tipo_membresia == "B":
    descuento = 0.15
elif tipo_membresia == "C":
    descuento = 0.2
else:
    descuento = 0

precio_final = precio_helado * (1 - descuento)

print("El precio final de su helado es:", precio_final)