Proceso Ejercicio6
	Escribir "Ingrese las horas semanales trabajadas: "
	Leer horas
	
	Si horas <= 40 Entonces
		Escribir "El pago es de: ", horas * 20
	SiNo
		Escribir "El pago es de: ", (horas - 40) * 25 + 800
	FinSi
FinProceso