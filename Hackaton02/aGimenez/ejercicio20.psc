Proceso ejercicio20
	numero1 = 0
	numero2 = 0
	numero3 = 0
	numero4 = 0
	contador = 0
	
	Escribir "Ingrese el Primer Numero"
	Leer numero1
	Escribir "Ingrese el Segundo Numero"
	Leer numero2
	Escribir "Ingrese el Tercer Numero"
	Leer numero3
	Escribir "Ingrese el Cuarto Numero"
	Leer numero4
	
	Escribir "Contando Pares"
	si numero1 mod 2==0 Entonces
		contador = contador + 1
	FinSi
	si numero2 mod 2==0 Entonces
		contador = contador + 1
	FinSi
	si numero3 mod 2==0 Entonces
		contador = contador + 1
	FinSi	
	si numero4 mod 2==0 Entonces
		contador = contador + 1
	FinSi
	Escribir "Hay " contador " pares"
	
	si numero1 > numero2 y numero1 > numero3 y numero1 > numero4 Entonces
		Escribir "El mayor es el " numero1
	FinSi
	si numero2 > numero1 y numero2 > numero3 y numero2 > numero4 Entonces
		Escribir "El mayor es el " numero2
	FinSi	
	si numero3 > numero1 y numero3 > numero2 y numero3 > numero4 Entonces
		Escribir "El mayor es el " numero3
	FinSi
	si numero4 > numero1 y numero4 > numero2 y numero4 > numero3 Entonces
		Escribir "El mayor es el " numero4
	FinSi
	
	si numero3 mod 2==0 Entonces
		Escribir "Como el 3ero es par, el cuadrado del 2do es: " numero2 * numero2
	FinSi	
	si numero1 < numero4 Entonces
		Escribir "Como el 1ero es menor que el 4to, la media de los cuatro es: " (numero1 + numero2 + numero3 + numero4) /4
	FinSi
	si numero2 > numero3 Entonces
		si numero3 > 49 y numero3 < 700 Entonces
			Escribir "Como el 2do es Mayor que el 3ero y el 3ero esta entre el 50 y 700, la suma de los cuatro es: " numero1 + numero2 + numero3 + numero4
		FinSi
	FinSi
FinProceso
