Algoritmo CalcularSueldo
	horasTrabajadas = 0
	sueldoPorHora = 0
	sueldoTotal = 0 
	
	sueldoPorHora = 20
	
	Escribir "Ingrese la cantidad de horas trabajadas en la semana:"
	Leer horasTrabajadas
	
	Si horasTrabajadas <= 40 Entonces
		sueldoTotal = horasTrabajadas * sueldoPorHora
	Sino
		sueldoTotal = (40 * sueldoPorHora) + ((horasTrabajadas - 40) * 25)
	FinSi
	
	Escribir "Su sueldo semanal es de: $" , sueldoTotal
	
FinAlgoritmo