Algoritmo Calculadora
	numero1 = 0
	numero2 = 0
	operacion = ""
	resultado = 0
	
	Escribir  "Dame el primer numero "
	Leer numero1
	Escribir "Dame el segundo numero"
	Leer  numero2
	Escribir "Dime la operacion q deseas realizar(suma,resta,multiplicacion,division)"
	Leer  operacion
	
	si operacion = "suma" Entonces
		resultado = numero1 + numero2
		Escribir "la suma de " numero1 " mas " numero2 " es " resultado
	SiNo
		si operacion == "resta" Entonces
			resultado = numero1 - numero2
			Escribir "la resta de " numero1 " mas " numero2 " es " resultado
		SiNo
			si operacion == "multiplicacion"
				resultado = numero1 * numero2
				Escribir "la multiplicacion de " numero1 " mas " numero2 " es " resultado
			SiNo
				si operacion == "division" Entonces
					resultado = numero1 / numero2
					Escribir "la divicion de " numero1 " mas " numero2 " es " resultado
			FinSi
		FinSi
	FinSi
FinSi
	
FinAlgoritmo
