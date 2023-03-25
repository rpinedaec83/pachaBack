Algoritmo ejer41
	//Hacer un algoritmo en Pseint que cumpla con la aproximación del número pi con la serie de Gregory-Leibniz. La formula que se debe aplicar es:
	
	//Pi = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...
	Definir i, num, conta como entero;
	Definir _pi como real;
	_pi <- 0;
	conta <- 0;
	
	Escribir "Ingrese un número";
	Escribir "Para calcular la sucesión de pi";
	Leer num;
	
	para i <-1 hasta num Con Paso 2 hacer
		
		si (conta mod 2 = 0) Entonces
			_pi <- _pi + (4 / i);
		SiNo
			_pi <- _pi - (4/ i);
		FinSi
		conta <- conta + 1;
		
	FinPara
	
	Escribir "Pi se aproxima a: ", _pi;
FinAlgoritmo
