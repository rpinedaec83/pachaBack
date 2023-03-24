Proceso ejercicio06
	horasTrabajadas = 0
	sueldoSemana = 0
	
	Escribir "Ingrese Cantidad de Horas Trabajadas"
	Leer horasTrabajadas
	
	si horasTrabajadas < 40 Entonces
		sueldoSemana = horasTrabajadas * 20
	FinSi
	si horasTrabajadas > 40 Entonces
		sueldoSemana = 40 * 20 + (horasTrabajadas - 40) * 25
	FinSi
	
	Escribir "Sueldo Semanal: $" sueldoSemana
FinProceso
