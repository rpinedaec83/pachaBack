Proceso Ejercicio11
	//Hacer un algoritmo en Pseint que
	//lea tres n�meros y diga cu�l es el mayor.

	Escribir "Ingresar primer numero"
	leer num1
	Escribir "Ingresar segundo numero"
	leer num2
	Escribir "Ingresar tercer numero"
	leer num3

	Si (num1 > num2 y num1 > num3) Entonces
		Escribir "El numero mayor es: " num1
	SiNo
		si (num2 > num3) Entonces
			Escribir "El numero mayor es: " num2
		SiNo
			Escribir "El numero mayor es: " num3
		FinSi
	FinSi
FinProceso
