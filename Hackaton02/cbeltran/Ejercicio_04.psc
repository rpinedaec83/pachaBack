Proceso Menor_mayor

	num1=0
	num2=0
	num3=0
	num_menor=0
	num_medio=0
	num_mayor=0

	Escribir "Ingrese el primer número:"
	Leer num1
	Escribir "Ingrese el segundo número:"
	Leer num2
	Escribir "Ingrese el tercer número:"
	Leer num3

	Si num1 <= num2 y num1 <= num3 Entonces
		num_menor = num1
		Si num2 <= num3 Entonces
			num_medio = num2
			num_mayor = num3
		SiNo
			num_medio = num3
			num_mayor = num2
		FinSi
	SiNo
		Si num2 <= num1 y num2 <= num3 Entonces
			num_menor = num2
			Si num1 <= num3 Entonces
				num_medio = num1
				num_mayor = num3
			SiNo
				num_medio = num3
				num_mayor = num1
			FinSi
		SiNo
			num_menor = num3
			Si num1 <= num2 Entonces
				num_medio = num1
				num_mayor = num2
			SiNo
				num_medio = num2
				num_mayor = num1
			FinSi
		FinSi
	FinSi

	Escribir "Los números ordenados de menor a mayor son: ", num_menor, " ", num_medio," ", num_mayor
FinProceso
