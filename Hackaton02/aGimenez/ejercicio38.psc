Proceso ejercicio38
	Definir numero1, contador, cantidad, suma, resto Como Entero;
	
	Escribir 'Ingrese un número';
	Leer numero1;
	contador = 0;
	cantidad = 0;
	Mientras (numero1 <> contador) Hacer
		contador = contador + 1;
		Si (contador <> numero1) Entonces
			resto = numero1 MOD contador;
			Si (resto = 0) Entonces
				cantidad = cantidad + contador;
			FinSi
		SiNo
			contador = numero1;
		FinSi
	FinMientras
	Escribir 'Suma de los divisores: ',cantidad;

	Si (numero1 = cantidad) Entonces
		Escribir 'Es perfecto';
	SiNo
		Escribir 'No es perfecto';
	FinSi
FinProceso
