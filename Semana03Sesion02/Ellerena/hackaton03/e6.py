num_zapatos = int(input("Ingrese la cantidad de zapatos que desea comprar: "))
precio_zapato = 80
descuento = 0

if num_zapatos > 30:
    descuento = 0.4
elif num_zapatos > 20:
    descuento = 0.2
elif num_zapatos > 10:
    descuento = 0.1

total_sin_descuento = num_zapatos * precio_zapato
total_con_descuento = total_sin_descuento * (1 - descuento)

print("El precio total de su compra es:", total_con_descuento)