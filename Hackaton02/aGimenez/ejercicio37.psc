Proceso ejercicio37
	a= 123922
	b= 870
	aux = 0
	Escribir "Ingresar dos numeros"
	Escribir "Numero Uno"
	Leer a
	Escribir "Numero Dos"
	Leer b
	Si (a<b)
		aux = a
		a = b
	FinSi
	Mientras b <> 0 Hacer
		resto = a%b
		a=b
		b=resto
	FinMientras
	Escribir "Resultado Final: " a;
FinProceso
