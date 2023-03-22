Proceso Ejercicio4
	//Hacer un algoritmo en Pseint que lea tres
	//n�meros enteros y los muestre de menor a mayor.
	Escribir "Ingrese primer numero entero"
	leer num1
	Escribir "Ingrese segundo numero entero"
	leer num2
	Escribir "Ingrese tercer numero entero"
	leer num3

	Si num1 > num2 Entonces
		si num2 > num3
			Escribir "De menor a mayor: " num3 ", " num2 ", " num1
		SiNo
			si num1 > num3 Entonces
				Escribir "De menor a mayor: " num2 ", " num3 ", " num1
			SiNo
				Escribir "De menor a mayor: " num2 ", " num1 ", " num3
			FinSi
		FinSi
	SiNo
		Si num1 > num3 Entonces
			Escribir "De menor a mayor: " num3 ", " num1 ", " num2
		SiNo
			si num2 > num3 Entonces
				Escribir "De menor a mayor: " num1 ", " num3 ", " num2
			SiNo
				Escribir "De menor a mayor: " num1 ", " num2 ", " num3
			FinSi
		FinSi
	FinSi
FinProceso
