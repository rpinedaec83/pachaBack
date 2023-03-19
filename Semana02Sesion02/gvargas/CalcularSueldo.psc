Algoritmo CalcularSueldo
	num = 0
	total = 0
	Escribir "Indique el número de horas que trabajo: "
	Leer num
	Si num > 40 Entonces
		total = num*25
		Escribir "Su sueldo será de: " total " dolares"
	SiNo
		total = num*20
		Escribir "Su sueldo será de: " total " dolares"
	FinSi
FinAlgoritmo
