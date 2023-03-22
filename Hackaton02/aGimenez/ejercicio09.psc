Proceso ejercicio09
	sueldo = 0
	sueldoAumento = 0
	
	Escribir "Ingrese Sueldo"
	Leer sueldo
	
	si sueldo > 2000 Entonces
		sueldoAumento = sueldo + (sueldo * 0.05)
		Escribir "Sueldo con Aumento: $" sueldoAumento
		Escribir "Aumento 5%"
	SiNo
		sueldoAumento = sueldo + (sueldo * 0.10)
		Escribir "Sueldo con Aumento: $" sueldoAumento
		Escribir "Aumento 10%"
	FinSi
	
FinProceso
