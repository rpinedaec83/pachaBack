Algoritmo ejericico_25
	Escribir "25. Hacer un algoritmo en Pseint para calcular el factorial de un número de una forma distinta."
	contador<-1;
	factorial<-1
	Escribir "Digite un numero para calcular su factorial";
	Leer num;
	
	Mientras contador < num
		contador<-contador+1
		factorial<-factorial*contador
		
	FinMientras
	
	Escribir "El factorial de ",num," es ",factorial
FinAlgoritmo
