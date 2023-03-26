Proceso e31
	Definir numero, suma_pares, suma_impares, cont_pares, cont_impares como Entero
	suma_pares <- 0
	suma_impares <- 0
	cont_pares <- 0
	cont_impares <- 0
	
	Para i <- 1 Hasta 10 Con Paso 1 Hacer
		Escribir("Ingrese un número: ")
		Leer numero
		Si (numero Mod 2 = 0) Entonces
			suma_pares <- suma_pares + numero
			cont_pares <- cont_pares + 1
		SiNo
			suma_impares <- suma_impares + numero
			cont_impares <- cont_impares + 1
		Fin Si
	Fin Para
	
	Si (cont_pares > 0) Entonces
		media_pares <- suma_pares / cont_pares
		Escribir"La media de los números pares es: ", media_pares
	Fin Si
	
	Si (cont_impares > 0) Entonces
		media_impares <- suma_impares / cont_impares
		Escribir "La media de los números impares es: ", media_impares
	Fin Si
FinProceso
