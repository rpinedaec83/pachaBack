Proceso Ejercicio4
	Definir n1, n2, n3 Como Entero;
	Escribir 'Ingrese tres números:';
	Leer n1;
	Leer n2;
	Leer n3;
	
	si (n1 < n2 y n1 < n3) entonces
		si (n2 < n3)
			Escribir n1," ", n2, " ", n3;
		SiNo
			Escribir n1," ", n3, " ",n2;
		FinSi
	FinSi
	
	si (n2 < n1 y n2 < n3) Entonces
		si (n1 < n3) Entonces
			Escribir n2," ", n1," ", n3;
		SiNo
			Escribir n2," ", n3," ", n1;
		FinSi
	FinSi
	
	si (n3 < n1 y n3 < n2) Entonces
		si (n1 < n2)
			Escribir n3," ", n1," ", n2;
		SiNo
			Escribir n3," ", n2," ", n1;
		FinSi
	FinSi
	
FinProceso
