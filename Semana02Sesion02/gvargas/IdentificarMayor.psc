Algoritmo IdentificarMayor
	num1 = 0
	num2 = 0
	num3 = 0
	Escribir "Escriba el número 1: "
	Leer num1
	Escribir "Escriba el número 2: "
	Leer num2
	Escribir "Escriba el número 3: "
	Leer num3
	Si (num1 > num2) y (num1 > num3) Entonces
		Escribir "El número mayor es: " num1
	SiNo
		Si (num2 > num1) y (num2 > num3) Entonces
			Escribir "El número mayor es: " num2
		SiNo
			Escribir "El número mayor es: " num3
		FinSi
	FinSi
FinAlgoritmo
