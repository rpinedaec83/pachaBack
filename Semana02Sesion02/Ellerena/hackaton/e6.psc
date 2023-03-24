Proceso e6
	Definir horas_trabajadas, salario_base, salario_total Como Real
    
    Escribir "Ingrese la cantidad de horas trabajadas en la semana:"
    Leer horas_trabajadas
    
    Si horas_trabajadas <= 40 Entonces
        salario_base = horas_trabajadas * 20
    Sino
        salario_base = 40 * 20 + (horas_trabajadas - 40) * 25
    FinSi
    
    salario_total <- salario_base
    
    Escribir "Su salario semanal es de: ", salario_total
    
FinProceso
