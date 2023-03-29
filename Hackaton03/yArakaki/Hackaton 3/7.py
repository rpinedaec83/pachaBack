# Pedir al usuario que ingrese su tipo de membresía
tipo_membresia = input("Ingrese su tipo de membresía (A, B o C): ")

# Determinar el descuento a aplicar
if tipo_membresia == "A":
    descuento = 0.1
elif tipo_membresia == "B":
    descuento = 0.15
elif tipo_membresia == "C":
    descuento = 0.2
else:
    print("Tipo de membresía inválido.")
    descuento = 0

# Pedir al usuario que ingrese el total de su compra
total_compra = float(input("Ingrese el total de su compra: "))

# Calcular el precio final con el descuento aplicado
precio_final = total_compra * (1 - descuento)

# Mostrar el precio final con el descuento aplicado
print("El precio final con descuento es: $", precio_final)
