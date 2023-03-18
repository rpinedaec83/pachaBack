Proceso Ejercicio8
	//Hacer un algoritmo en Pseint para calcular
	//el promedio de tres notas y
	//determinar si el estudiante aprob� o no.

	suma = 0
	promedio = 0

	Escribir "Ingresar nota 1"
	Leer nota1
	Escribir "Ingresar nota 2"
	Leer nota2
	Escribir "Ingresar nota 3"
	Leer nota3

	promedio = (nota1 + nota2 + nota3) / 3

	si promedio < 11 Entonces
		Escribir "DESAPROBADO, promedio ", promedio
	SiNo
		si promedio >= 11 Entonces
			Escribir "APROBADO, promedio ", promedio
		FinSi
	FinSi
FinProceso
