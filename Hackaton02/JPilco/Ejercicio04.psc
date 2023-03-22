//Hacer un algoritmo en Pseint que lea tres números enteros y los muestre de menor a mayor.
Proceso Ejercicio04
	Definir num1, num2, num3 Como Entero
	Escribir "Ingrese el primer numero"
	Leer num1
	Escribir "Ingrese el segundo numero"
	Leer num2
	Escribir "Ingrese el tercer numero"
	Leer num3
	
	Si Num1<=num2 Y num1 <= num3 Entonces
		Escribir num1
		
		Si Num2<=num3  Entonces
			Escribir num2
			Escribir num3
		SiNo
			Escribir num3
			Escribir num2
		FinSi
		
	SiNo
		Si Num2<=num1 Y num2 <= num3 Entonces
			Escribir num2
			
			Si Num1<=num3 Entonces
				Escribir num1
				Escribir num3
			SiNo
				Escribir num3
				Escribir num1
			FinSi
			
	Sino 
				Escribir num3
				
				Si Num1<=num2  Entonces
					Escribir num1
					Escribir num2
				SiNo
					Escribir num2
					Escribir num1
				FinSi
			FinSi
			
		
	Fin Si
	
	


	
FinProceso
