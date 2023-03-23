Algoritmo Calculadora
	PrimerNumero = 0
	SegundoNumero = 0
	Operacion = 1000
	Resultado = 0
	
	Mientras Operacion <> 0   Hacer
		
		Escribir "Inserte la operacion que deseas realizar:"
		Escribir "(1)Suma"
		Escribir "(2)Resta"
		Escribir "(3)Multiplicacion"
		Escribir "(4)Division"
		Escribir "(0)Salir"
		leer Operacion
		
		Si Operacion <> 0 Entonces
			
			Escribir "Inserte el primer numero"
			leer PrimerNumero
			Escribir "Inserte el segundo numero"
			leer SegundoNumero
			
			Segun Operacion Hacer
				1:
					Resultado = PrimerNumero + SegundoNumero
					Escribir "La suma de " PrimerNumero " mas " SegundoNumero " es " Resultado
				2:
					Resultado = PrimerNumero - SegundoNumero
					Escribir "La resta de " PrimerNumero " menos " SegundoNumero " es " Resultado
				3:
					Resultado = PrimerNumero * SegundoNumero
					Escribir "La multiplicacion de " PrimerNumero " por " SegundoNumero " es " Resultado
				4:
					Resultado = PrimerNumero / Numero2
					Escribir "La division de " PrimerNumero " entre " SegundoNumero " es " Resultado
				De Otro Modo:
					Escribir "Command not founded"
			Fin Segun
		SiNo
			
		Fin Si
	Fin Mientras
	
	
	
FinAlgoritmo
