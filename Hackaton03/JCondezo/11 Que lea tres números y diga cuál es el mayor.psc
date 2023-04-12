//que lea tres números y diga cuál es el mayor.

Algoritmo sin_titulo
	Definir A,B COMO ENTERO
	Escribir "Ingrese Primer Numero" 
	leer a
	Escribir "Ingrese Segundo Numero" 
	leer b
	
	si a<>b y a<>c y b<>c Entonces
		si a>b Entonces
			si a>c Entonces
				Escribir "el NUmero mayor es: " a
			SiNo
				Escribir "El Numero Mayor es: " c
			FinSi
		SiNo
			si b>c entonces
				Escribir "El Numero mayor es: ", b
			SiNo
				Escribir "El numero mayor es: ", c
 			FinSi
		FinSi
		
	FinSi

FinAlgoritmo
