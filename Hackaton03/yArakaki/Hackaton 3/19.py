def calcular_salario(identificador, dias_trabajados):
    if identificador == 1:  # Cajero
        salario_diario = 56
    elif identificador == 2:  # Servidor
        salario_diario = 64
    elif identificador == 3:  # Preparador de mezclas
        salario_diario = 80
    elif identificador == 4:  # Mantenimiento
        salario_diario = 48
    else:
        return "Identificador de empleado inválido."
    salario_semana = dias_trabajados * salario_diario
    return f"El salario correspondiente para el empleado con identificador {identificador} que trabajó {dias_trabajados} días es de ${salario_semana}."

# Ejemplo de uso
identificador = int(input("Ingrese el número identificador del empleado: "))
dias_trabajados = int(input("Ingrese la cantidad de días trabajados en la semana (máximo 6 días): "))
print(calcular_salario(identificador, dias_trabajados))
