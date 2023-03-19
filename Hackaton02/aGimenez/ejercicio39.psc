Proceso ejercicio39
	Definir i, numero1, contador como entero;
	Definir pi1 como real;
	pi1 = 0;
	contador = 0;
	
	Escribir "Ingrese un número";
	Escribir "Para calcular la sucesión de pi";
	Leer numero1;
	
	Para i = 1 hasta numero1 Con Paso 2 hacer
		
		si (conta mod 2 == 0) Entonces
			pi1 = pi1 + (4 / i);
		SiNo
			pi1 = pi1 - (4/ i);
		FinSi
		contador = contador + 1;
		
	FinPara
	
	Escribir "Pi se aproxima a: ", pi1;
FinProceso
