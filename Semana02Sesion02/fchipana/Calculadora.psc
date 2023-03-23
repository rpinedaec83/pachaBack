Proceso Calculadora
	Numero1 = 0
	Numero2 = 0
	Operacion = ""
	Resultado = 0
	
	Escribir "Dame el primer numero"
	Leer  Numero1
	Escribir "Dame el segundo numero"
	leer Numero2
	Escribir "Dime la operacion que deseas realizar (Suma, Resta, Multiplicacion, Division)"
	leer Operacion
	
	si Operacion == "Suma" Entonces
		Resultado = Numero1 + Numero2
		Escribir "La suma de " Numero1 " mas " Numero2 " es " Resultado
	SiNo
		si Operacion == "Resta" Entonces
			Resultado = Numero1 - Numero2
			Escribir "La resta de " Numero1 " menos " Numero2 " es " Resultado
		SiNo
			si Operacion == "Multiplicacion" Entonces
				Resultado = Numero1 * Numero2
				Escribir "La multiplicacion de " Numero1 " por " Numero2 " es " Resultado
			SiNo
				si Operacion == "Division" Entonces
					Resultado = Numero1 / Numero2
					Escribir "La  division de  " Numero1 " entre " Numero2 " es " Resultado
				FinSi
				
			FinSi
			
		FinSi
	
	FinSi
	
FinProceso
