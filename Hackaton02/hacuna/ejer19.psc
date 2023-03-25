Algoritmo Heladeria
	
	Escribir "Ingrese el número identificador del empleado (56, 64, 80 o 48): "
	Leer identificador
	
	Escribir "Ingrese la cantidad de días que trabajó en la semana: "
	Leer dias_trabajados
	
	Si identificador = 56 Entonces
		salario_diario = 56
		cargo = "Cajero"
	Sino Si identificador = 64 Entonces
			salario_diario = 64
			cargo = "Servidor"
		Sino Si identificador = 80 Entonces
				salario_diario = 80
				cargo = "Preparador de mezclas"
			Sino Si identificador = 48 Entonces
					salario_diario = 48
					cargo = "Mantenimiento"
				Sino
					Escribir "Error: número identificador inválido."
				FinSi
			FinSi
		FinSi
	FinSi	
	
	Si identificador == 48 o identificador == 80 o identificador ==64 o identificador==56 Entonces
		pago_semanal = salario_diario * dias_trabajados
		Escribir "El empleado de", cargo, "con número identificador", identificador, "trabajó", dias_trabajados, "días y debe recibir un pago de $", pago_semanal
	Sino
		Escribir "Error: número identificador inválido."
	FinSi
	
FinAlgoritmo



