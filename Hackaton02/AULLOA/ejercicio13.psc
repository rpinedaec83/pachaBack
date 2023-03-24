Algoritmo ejercicio13
	//Hacer un algoritmo en Pseint que lea un entero positivo del 1 al diez y determine si es un número primo.
	Definir n,i Como Entero
	cont <- 0
	Escribir "ingrese un numero del 1 al 10"
	Leer n
	
	Para i<-1 Hasta n Hacer
		si n%i=0 Entonces
			cont <- cont + 1
		FinSi
	FinPara
	
	si cont = 2 Entonces
		Escribir "es primo"
	SiNo
		Escribir "no es primo"
	FinSi
	
FinAlgoritmo
