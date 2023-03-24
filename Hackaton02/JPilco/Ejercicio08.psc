//Hacer un algoritmo en Pseint para calcular el promedio de tres notas y determinar si el estudiante aprobó o no.
Proceso Ejercicio08
	Definir nota1,nota2,nota3,promedio Como Real
	Escribir "********Promedio de notas********** "
	Escribir "Ingrese la nota 1: "
	leer nota1
	Escribir "Ingrese la nota 2: "
	leer nota2
	Escribir "Ingrese la nota 3: "
	leer nota3
	promedio=(nota1+nota2+nota3)/3
	Si promedio>=10.5 Entonces
		Escribir "El estudiante aprobo "
	SiNo
		Escribir "El estudiante desaprobo "
	Fin Si
	
	
	
FinProceso
