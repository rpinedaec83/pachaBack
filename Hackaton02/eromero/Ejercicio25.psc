Proceso Ejercicio25
	Escribir "Introduce un nùmero: "
	Definir num1 Como Entero
	Leer num1
	Escribir Factorial(num1)	
FinProceso

Funcion valor <- Factorial(n)
	Si n = 0 Entonces
		valor <-1
	Sino
		valor <- n * Factorial(n-1)
	FinSi
FinFuncion	