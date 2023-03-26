//lea un entero positivo del 1 al diez y al 9 y 
//determine si es un número primo.
Algoritmo sin_titulo
	escribir "ingrese un numero positivo"
	leer a
	si a<0 y a >10 Entonces 
		escribir "el numero es negativo o supero el maximo permitido 10"
	sino 
		para i<- 1 hasta a Hacer
			si a%10=0 Entonces
				cont<-cont+1
				
			FinSi
		FinPara
		si cont=2 Entonces
			Escribir a, "es un Primo"
		SiNo
			escribir a " no es un proimo"
			
		FinSi
	FinSi
FinAlgoritmo
