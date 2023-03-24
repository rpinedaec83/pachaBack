//Hacer un algoritmo en Pseint que lea un entero positivo del 1 al diez y al 9 y determine si es un número primo.
Proceso Ejercicio14
	Definir numero Como Entero
	definir primo Como Logico
	Escribir "Ingrese numero: "
	Leer numero
	Si numero<1 o numero>10 Entonces
		Escribir "El numero ingresado no es valido" 
	SiNo
		
		
	
	primo=Verdadero
	Para i<-2 Hasta numero-1 Con Paso 1 Hacer
		Si numero%1==0 Entonces
			primo=Falso
	
		Fin si
	Fin para
	
	Si primo Entonces
		Escribir "El numero es primo"
	SiNo
		Escribir "El numero no es primo"
	Fin Si
FinSi

	

	
FinProceso

