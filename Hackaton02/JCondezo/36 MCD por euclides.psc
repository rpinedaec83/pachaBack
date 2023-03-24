//conseguir el M.C.D de un número por medio del algoritmo de Euclides.//
Algoritmo sin_titulo
	
	a=162078;
	b=960;
	temporal=0;
	
	Si(a<b)
		temporal=a;
		a=b;
		b=temporal;
	FinSi
	
	Mientras b<>0 Hacer
	
		resto=a%b;
		Escribir "Division " a/b;
		Escribir "Resto " a%b;
	
		a=b;
	
		b=resto;
		Escribir a;
	FinMientras
	
	Escribir "Resultado Final: " a; 
	
FinProceso
	
FinAlgoritmo
