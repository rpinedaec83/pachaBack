Algoritmo ejercicio8
	//Hacer un algoritmo en Pseint para calcular el promedio de tres notas y determinar si el estudiante aprobó o no.
	Definir n1,n2,n3,prom Como Real
	Escribir "ingrese las notas del alumno del 0 al 20: "
    Leer n1,n2,n3
    prom <- (n1+n2+n3)/3
    Escribir prom
	Si (prom>=13) Entonces
		Escribir "aprobado"
	SiNo
		Escribir "desaprobado"
	FinSi
FinAlgoritmo