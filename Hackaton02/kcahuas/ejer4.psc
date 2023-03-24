Algoritmo ejer4
	//Hacer un algoritmo en Pseint que lea tres números enteros y los muestre de menor a mayor.
	Escribir "escribe tu primer numero"
	leer num1
	Escribir "escribe tu segundo numero"
	leer num2
	Escribir "escribe tu tercer numero"
	leer num3
	si num1>num2 y num1>num3   Entonces
		Escribir "tu primer numero es mayor",num1
	SiNo
		si	num2>num1 y num2>num3 Entonces
			Escribir "tu segundo numero es el mayor", num2
		SiNo 
			si	num3>num1 y num3>num2 Entonces
				Escribir "tu tercer numero es el mayor", num3
				
			FinSi
			
		FinSi
	FinSi
	
FinAlgoritmo
