Proceso Aumento_salario

    salarioActual=0.0
	salarioNuevo =0.0

	Escribir "Ingrese el salario actual del trabajador: "
	Leer salarioActual

	Si salarioActual > 2000 Entonces
		salarioNuevo = salarioActual * 1.1
	Sino
		salarioNuevo = salarioActual * 1.05
	FinSi

	Escribir "El salario nuevo del trabajador es: ", salarioNuevo
FinProceso
