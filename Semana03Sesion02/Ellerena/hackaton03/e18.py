cantidad = int(input("Ingrese la cantidad de CDs a vender: "))
precio_total = 0

if cantidad < 1:
    print("Cantidad inválida. Debe ser un número entero positivo mayor que cero.")
else:
    if cantidad < 10:
        precio_total = cantidad * 10
    elif cantidad < 100:
        precio_total = cantidad * 8
    elif cantidad < 500:
        precio_total = cantidad * 7
    else:
        precio_total = cantidad * 6

    ganancia_vendedor = precio_total * 0.0825
    precio_total += ganancia_vendedor

    print(f"Precio total para el cliente: ${precio_total:.2f}")
    print(f"Ganancia para el vendedor: ${ganancia_vendedor:.2f}")
