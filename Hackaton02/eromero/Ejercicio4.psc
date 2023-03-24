Proceso Ejercicio4
	Escribir "Ingrese el primer número: "
	Leer num1
	Escribir "Ingrese el segundo número: "
	Leer num2
	Escribir "Ingrese el tercer número: "
	Leer num3
	
	Si num1 < num2 y num1 < num3 Entonces
		Escribir num1
		Si num2 < num3 Entonces
			Escribir num2
			Escribir num3
		Sino
			Escribir num3
			Escribir num2
		Fin Si
	Sino Si num2 < num1 y num2 < num3 Entonces
			Escribir num2
			Si num1 < num3 Entonces
				Escribir num1
				Escribir num3
			Sino
				Escribir num3
				Escribir num1
			Fin Si
		Sino
			Escribir num3
			Si num1 < num2 Entonces
				Escribir num1
				Escribir num2
			Sino
				Escribir num2
				Escribir num1
			Fin Si
		Fin Si
	Fin Si
FinProceso