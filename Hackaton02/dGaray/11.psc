Proceso sin_titulo
	Definir numero1,numero2,numero3 Como Entero
	Escribir "ingresa 3 numeros: "
	Leer numero1, numero2, numero3
	Si (numero1 > numero2 y numero1 > numero3) Entonces
		Escribir "el mayor es: ", numero1
	FinSi
	Si (numero2 > numero1 y numero2 > numero3) Entonces
		Escribir "el mayor es: ", numero2
	FinSi
	Si (numero3 > numero1 y numero3 > numero2) Entonces
		Escribir "el mayor es: ", numero3
	FinSi
FinProceso
