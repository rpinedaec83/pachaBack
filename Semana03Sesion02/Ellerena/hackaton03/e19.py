def calcular_salario(identificador, dias_trabajados):
    salarios = {56: "Cajero", 64: "Servidor", 80: "Preparador de mezclas", 48: "Mantenimiento"}
    if identificador not in salarios:
        print("Identificador de empleado inválido")
        return
    salario_diario = salarios[identificador]
    salario_semanal = salario_diario * dias_trabajados
    print(f"El salario para el empleado {salario_diario} por {dias_trabajados} días es {salario_semanal}$")

identificador = int(input("Ingrese el identificador del empleado (56, 64, 80, 48): "))
dias_trabajados = int(input("Ingrese la cantidad de días trabajados (1-6): "))
calcular_salario(identificador, dias_trabajados)
