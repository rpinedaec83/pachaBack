Proceso Ejercicio15
	//Hacer un algoritmo en Pseint que
	//convierta cent�metros a pulgadas
	//y libras a kilogramos.
	Escribir "Selecciona opci�n 1 o 2"
	Escribir "1: Centimetros a pulgadas"
	Escribir "2: Libras a kilogramos"
	leer opc

	Segun opc Hacer
		1:
			Escribir "Ingresar valor"
			leer num
			Escribir num " cm es igual a " num / 2.54 " pulgadas"
		2:
			Escribir "Ingresar valor"
			leer num
			Escribir num " libras es igual a " num / 2.205 " kg"

		De Otro Modo:
			Escribir "Opci�n No V�lida"
	Fin Segun
FinProceso
