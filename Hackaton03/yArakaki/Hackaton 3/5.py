cantidad = int(input("Ingrese la cantidad de zapatos que desea comprar: "))
precio_unitario = 80

if cantidad > 30:
    descuento = 0.4
elif cantidad > 20:
    descuento = 0.2
elif cantidad > 10:
    descuento = 0.1
else:
    descuento = 0

precio_total = cantidad * precio_unitario
descuento_total = precio_total * descuento
precio_con_descuento = precio_total - descuento_total

print("El precio total es:", precio_total)
print("El descuento es:", descuento_total)
print("El precio con descuento es:", precio_con_descuento)
