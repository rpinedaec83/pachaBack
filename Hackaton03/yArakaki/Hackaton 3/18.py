def calcular_precio(cantidad):
    if cantidad < 10:
        precio_unitario = 10
    elif cantidad < 100:
        precio_unitario = 8
    elif cantidad < 500:
        precio_unitario = 7
    else:
        precio_unitario = 6
    precio_total = cantidad * precio_unitario
    ganancia_vendedor = round(precio_total * 0.0825, 2)
    return precio_total, ganancia_vendedor

# Ejemplo de uso
cantidad = int(input("Ingrese la cantidad de CD vírgenes que desea comprar: "))
precio_total, ganancia_vendedor = calcular_precio(cantidad)
print(f"El precio total de la compra para el cliente es: ${precio_total}")
print(f"La ganancia del vendedor es: ${ganancia_vendedor}")
