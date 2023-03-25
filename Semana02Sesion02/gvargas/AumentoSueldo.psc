Algoritmo AumentoSueldo
	sueldo = 0
	aumento = 0
	Escribir "Escriba su sueldo actual: "
	Leer sueldo
	Si sueldo > 2000 Entonces
		aumento = sueldo*0.05
		Escribir "Tendrá un aumnto de: " aumento " dolares"
		Escribir "Su nuevo sueldo es: " sueldo+aumento " dolares"
	SiNo
		aumento = sueldo*0.1
		Escribir "Tendrá un aumnto de: " aumento " dolares"
		Escribir "Su nuevo sueldo es: " sueldo+aumento " dolares"
	FinSi
FinAlgoritmo
