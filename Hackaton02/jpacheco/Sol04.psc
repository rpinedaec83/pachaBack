Algoritmo sin_titulo
	//4.-Hacer un algoritmo en Pseint que lea tres números enteros y los muestre de menor a mayor.
		Escribir 'Ingrese tres números:';
		Leer num1;
		Leer num2;
		Leer num3;
		
		si (num1 < num2 y num1 < num3) entonces
			si (num2 < num3)
				Escribir num1," ", num2, " ", num3;
			SiNo
				Escribir num1," ", num3, " ",num2;
			FinSi
		FinSi
		
		si (num2 < num1 y num2 < num3) Entonces
			si (num1 < num3) Entonces
				Escribir num2," ", num1," ", num3;
			SiNo
				Escribir num2," ", num3," ", num1;
			FinSi
		FinSi
		
		si (num3 < num1 y num3 < num2) Entonces
			si (num1 < num2)
				Escribir num3," ", num1," ", num2;
			SiNo
				Escribir num3," ", num2," ", num1;
			FinSi
		FinSi
		

FinAlgoritmo
