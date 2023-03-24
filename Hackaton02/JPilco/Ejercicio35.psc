//Hacer un algoritmo en Pseint que nos permita saber cuál es el número mayor y menor, se debe ingresar sólo veinte números.
Proceso Ejercicio35
	mayor=0
	menor=0
	Para i=1 Hasta 20 Hacer
		escribir "El numero es ",i,":"
		leer numeroIngresado
		si numeroIngresado>mayor Entonces
			mayor=numeroIngresado
		FinSi
		si numeroIngresado<menor Entonces
			menor=numeroIngresado
		FinSi
	FinPara
	Escribir "El numero mayor es : ", mayor
	Escribir "El numero menor es: ", menor
	
FinProceso
