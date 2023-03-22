Algoritmo sin_titulo
	//35.-Hacer un algoritmo en Pseint que nos permita saber cuál es el número mayor y menor, se debe ingresar sólo veinte números.
	Leer num;
	max <- num;
	min <- num;
	Para i<-1 Hasta 20 Hacer
		Leer num;
		Si (num>max) Entonces
			max <- num;
		FinSi
		Si (num<min) Entonces
			min <- num;
		FinSi
	FinPara
	Escribir 'El número menor es: ',min;
	Escribir 'El número mayor es: ',max;
	
FinAlgoritmo
