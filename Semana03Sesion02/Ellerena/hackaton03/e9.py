salario_actual = float(input("Ingrese su salario actual: "))

if salario_actual > 2000:
    aumento = 0.05
else:
    aumento = 0.1

salario_nuevo = salario_actual * (1 + aumento)

print("Su nuevo salario es:", salario_nuevo)