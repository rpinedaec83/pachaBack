Algoritmo ejercicio06
	Escribir "Ingrese cantidad de horas trabajadas"
	leer horas_trabajadas
	si horas_trabajadas <= 40 entonces
		sueldo_semanal <- horas_trabajadas * 20
	sino
		horas_normales <- 40
		horas_extras <- horas_trabajadas - 40
		sueldo_normales <- horas_normales * 20
		sueldo_extras <- horas_extras * 25
		sueldo_semanal <- sueldo_normales + sueldo_extras
	fin si
	escribir "El sueldo semanal del trabajador es de: $", sueldo_semanal
FinAlgoritmo
