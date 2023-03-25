Algoritmo PagoEmpleado
	Definir identificador, dias_trabajados Como Entero
	Definir salario_diario, salario_semanal Como Real
	
	
	Escribir "Ingrese el número identificador del empleado:"
	Leer identificador
	Escribir "Ingrese la cantidad de días que trabajó en la semana:"
	Leer dias_trabajados
	
	Si dias_trabajados > 0 Y dias_trabajados <= 6 Entonces
		Si identificador = 1 Entonces
			salario_diario = 56
		Sino
			Si identificador = 2 Entonces
				salario_diario = 64
			Sino
				Si identificador = 3 Entonces
					salario_diario = 80
				Sino
					Si identificador = 4 Entonces
						salario_diario = 48
					Sino
						Escribir "El número identificador ingresado no es válido"
						
					FinSi
				FinSi
			FinSi
		FinSi
		
		salario_semanal = dias_trabajados * salario_diario
		
		Escribir "El empleado con número identificador ", identificador, " trabajó ", dias_trabajados, " días"
		Escribir "El salario diario correspondiente es: $", salario_diario
		Escribir "El salario semanal correspondiente es: $", salario_semanal
	Sino
		Escribir "La cantidad de días ingresada no es válida"
	FinSi
	
FinAlgoritmo
