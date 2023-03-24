Proceso ejercicio19
	sueldoSemanal = 0
	diasTrabajados = 0
	nroIdentificadorEmpleado = 0
	
	Escribir "Ingrese el Numero de Identificador de Empleado"
	Escribir "1- Cajero"
	Escribir "2- Servidor"
	Escribir "3- Preparador de Mezclas"
	Escribir "4- Mantenimiento"
	Leer nroIdentificadorEmpleado
	
	Escribir "Dias Trabajadas (Max 6): "
	Leer diasTrabajados
	
	Segun nroIdentificadorEmpleado Hacer
		1:
			sueldoSemanal = diasTrabajados * 56
		2:
			sueldoSemanal = diasTrabajados * 64
		3:
			sueldoSemanal = diasTrabajados * 80
		4:
			sueldoSemanal = diasTrabajados * 48
	FinSegun
	
	Escribir "El Empleado recibe esta semana $" sueldoSemanal
FinProceso
