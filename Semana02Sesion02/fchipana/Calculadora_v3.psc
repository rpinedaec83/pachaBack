Proceso Calculadora_v3
	Numero1 = 0
	Numero2 = 0
	Operacion = 9
	Resultado = 0
	
	Mientras Operacion <> 0 hacer
	
		Escribir "Dame el primer numero"
		Leer  Numero1
		Escribir "Dame el segundo numero"
		leer Numero2
		Escribir "Dime la operacion que deseas realizar:"
		Escribir "Digita 1 para Suma"
		Escribir "Digita 2 para Resta"
		Escribir "Digita 3 para Multiplicacion"
		Escribir "Digita 4 para Division"
		Escribir "Digita 0 para salir"
		
		leer Operacion
		
		Segun Operacion Hacer
			1:
				Resultado = Numero1 + Numero2
				Escribir "La suma de " Numero1 " mas " Numero2 " es " Resultado
			2:
				Resultado = Numero1 - Numero2
				Escribir "La resta de " Numero1 " menos " Numero2 " es " Resultado
			3:
				Resultado = Numero1 * Numero2
				Escribir "La multiplicacion de " Numero1 " por " Numero2 " es " Resultado
			4:
				Resultado = Numero1 / Numero2
				Escribir "La  division de  " Numero1 " entre " Numero2 " es " Resultado
			De Otro Modo:
				Escribir "Opcion No valida."
		Fin Segun
	
	FinMientras
	
FinProceso
