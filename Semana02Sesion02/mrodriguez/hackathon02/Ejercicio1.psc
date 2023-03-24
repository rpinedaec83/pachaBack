Proceso Ejercicio1
	//Hacer un algoritmo en Pseint que lea un número 
	//por el teclado y determinar si tiene tres dígitos.
	Definir num Como Entero
	Escribir "Ingrese un numero de tres digitos"
	leer num

	Si num < 0 //Para leer negativos
		num = num*(-1)
	FinSi
	Si num >= 100 Y num <= 999
		Escribir "El numero " num " tiene tres digitos"
	SiNo
		Escribir "El numero " num " NO tiene tres digitos"
	FinSi
FinProceso
