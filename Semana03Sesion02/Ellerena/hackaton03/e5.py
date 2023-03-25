
precio_zapato = 80


cantidad_zapatos = int(input("¿Cuántos zapatos desea comprar? "))


precio_total = cantidad_zapatos * precio_zapato


if cantidad_zapatos > 30:
    descuento = 0.4
elif cantidad_zapatos > 20:
    descuento = 0.2
elif cantidad_zapatos > 10:
    descuento = 0.1
else:
    descuento = 0

precio_descuento = precio_total - (precio_total * descuento)

print("El precio total de la compra es:", precio_total)
print("El descuento aplicado es:", descuento * 100, "%")
print("El precio total con descuento es:", precio_descuento)
