Proceso Sueldo_semanal

	horasTrabajadas=0
	horasExtras=0
	sueldoTotal=0.0	
	sueldoTotal = 0.0
	sueldoHora = 20.0 
	
	Escribir "Ingrese las horas trabajadas en la semana: "
	Leer horasTrabajadas
	
	Si horasTrabajadas > 40 Entonces
		horasExtras = horasTrabajadas - 40
		sueldoTotal = 40 * sueldoHora + horasExtras * 25
	Sino
		sueldoTotal = horasTrabajadas * sueldoHora
	FinSi
	

	Escribir "El sueldo semanal es de: $", sueldoTotal
FinProceso
