Algoritmo sin_titulo
	//40.-Hacer un algoritmo en Pseint que cumpla con la aproximación del número pi con la serie de Nilakantha. La formula que se debe aplicar es:
	//Pi = = 3 + 4/(234) - 4/(456) + 4/(678) - 4/(8910) + 4/(101112) - (4/(121314) .
	_pi <- 0;
	conta <- 0;
	Escribir 'Ingrese un número';
	Escribir 'Para calcular la sucesión de pi';
	Leer num;
	Para i<-2 Hasta num Con Paso 2 Hacer
		Si (conta MOD 2=0) Entonces
			_pi <- _pi+(4/(i*(i+1)*(i+2)));
		SiNo
			_pi <- _pi-(4/(i*(i+1)*(i+2)));
		FinSi
		conta <- conta+1;
	FinPara
	Escribir 'Pi se aproxima a: ',_pi+3;
FinAlgoritmo
