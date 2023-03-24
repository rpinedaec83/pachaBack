//Hacer un algoritmo en Pseint para calcular la serie de Fibonacci.
Proceso Ejercicio36
	Definir n,a,b,c Como Entero
	Escribir "Inglerse la cantidad de terminos de la serie de fibonacci a calcular "
	Leer n
	a=0
	b=1
	Escribir a
	Escribir b
	
	Mientras n>2 Hacer
		c=a+b
		Escribir c
		a=b
		b=c
		n=n-1
	FinMientras
	
FinProceso
