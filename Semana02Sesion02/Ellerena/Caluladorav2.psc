Proceso Caluladorav2
	numero1 = 0
	numero2 = 0
	operacion = 0
	resultado = 0
	operacion2 = 0
	Escribir  "Dame el primer numero "
	Leer numero1
	Escribir "Dame el segundo numero"
	Leer  numero2
	
	Escribir "Dime la operacion q deseas realizar"
	Escribir "Digita 1 para suma"
	Escribir "Digita 2 para resta"
	Escribir "Digita 3 para multiplicacion"
	Escribir "Digita 4 para dividir"
	
	Leer  operacion2
	Segun operacion2 Hacer
		1:
			resultado = numero1 + numero2
			Escribir "la suma de " numero1 " mas " numero2 " es " resultado
		2:
			resultado = numero1 - numero2
			Escribir "la resta de " numero1 " mas " numero2 " es " resultado
		3:
			resultado = numero1 * numero2
			Escribir "la multiplicacion de " numero1 " mas " numero2 " es " resultado
		4:
			resultado = numero1 / numero2
			Escribir "la divicion de " numero1 " mas " numero2 " es " resultado
		De Otro Modo:
			Escribir "la operacion no es valida"
	FinSegun
	
FinProceso
