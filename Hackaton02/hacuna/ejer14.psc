Algoritmo ejercicio14
	Escribir "Ingrese un numero"
	leer numero1
	Para i<-1 hasta numero1 Hacer
		Si numero1%i=0 Entonces
			cont<- cont+1
		FinSi
	FinPara
	
	Si cont=2  Entonces
		Escribir numero1, " es un numero primo"
	SiNo
		Escribir numero1, " no es un numero primo"
	FinSi
FinAlgoritmo
