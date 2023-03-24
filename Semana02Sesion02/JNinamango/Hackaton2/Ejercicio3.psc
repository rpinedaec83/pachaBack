Proceso Ejercicio3
	Definir num Como entero;
	
	Escribir 'Ingrese un número:';
	Leer num;
	
	Si (num mod 10 = 4) Entonces
		Escribir "El número termina en 4";
	SiNo
		si(num mod 10 = -4) entonces
			Escribir "El número termina en 4";
		SiNo
			Escribir "El número no termia en 4";
		finsi
	FinSi
	
FinProceso
