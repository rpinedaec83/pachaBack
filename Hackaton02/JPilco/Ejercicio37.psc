//Hacer un algoritmo en Pseint para conseguir el M.C.D de un número por medio del algoritmo de Euclides.
Proceso Ejercicio37
	Definir a,b,r Como Entero
	Escribir "Introdusca el primer numero: "
	Leer a
	Escribir "Introdusca el segundo numero: "
	Leer b
	Mientras b<>0 Hacer
		r=a mod b
		a=b
		b=r
	FinMientras
	Escribir "El MCD de los dos numeros es: ", a
	
FinProceso
