Proceso Calculadora
	Numero1 = 0
	Numero2 = 0
	Operacion = -1
	Resultado = 0
	
	Mientras Operacion <> 0 Hacer
		Escribir "Ingresa el primer numero"
		Leer Numero1
		Escribir "Ingresa el segundo numero"
		Leer Numero2
		Escribir "Ingresa la operacion que desea realizar"
		Escribir "1 Suma"
		Escribir "2 Resta"
		Escribir "3 Multiplicacion"
		Escribir "4 Division"
		Escribir "0 Para Salir"
		Leer Operacion
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
				Escribir "La division de " Numero1 " entre " Numero2 " es " Resultado
			De Otro Modo:
				Escribir "Opcion No Valida"
		Fin Segun
	FinMientras
	
FinProceso
