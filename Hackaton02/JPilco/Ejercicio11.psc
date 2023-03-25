//Hacer un algoritmo en Pseint que lea tres números y diga cuál es el mayor.
Proceso Ejercicio11
	Definir num1,num2,num3, mayior Como Entero
	Escribir "Ingrese el primer numero: "
	Leer num1
	Escribir "Ingrese el segundo numero: "
	Leer num2
	Escribir "Ingrese el tercer numero: "
	Leer num3
	Si num1>=num2 Y num1>=num3 Entonces
		mayior=num1
	SiNo
		Si num2>=num1 Y num2>=3 Entonces
			mayior=num2
		SiNo
			mayior=num3
		Fin Si
	Fin Si
	Escribir "El mayor de los tres numeros es: " mayior	
	
FinProceso
