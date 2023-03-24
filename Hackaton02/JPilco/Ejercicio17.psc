//Hacer un algoritmo en Pseint donde se ingrese una hora y nos calcule la hora dentro de un segundo.
Proceso Ejercicio17
	Definir hora,minuto,segundoo Como Entero
	Escribir "Ingrese la hora en formato de 24 horas "
	Leer hora
	Escribir "Ingrese el minuto "
	Leer minuto
	Escribir "Ingrese el segundo "
	Leer segundoo
	segundoo=segundoo+1
	Si segundoo=60 Entonces
		segundoo=0
		minuto=minuto+1
		Si minuto=60 Entonces
			minuto=0
			hora=hora+1
			Si hora=24 Entonces
				hora=0
			FinSi
		FinSi
	FinSi
	Escribir "La hora dentro de un segundo es: " hora ":" minuto ":" segundoo 
	
	
FinProceso
