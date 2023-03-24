Proceso sin_titulo
	Definir numero como entero
	Escribir "Brindame un numero"
	Leer numero
	Si numero <1 Entonces
		escribir "El numero debe ser positivo"
	Sino
		resultado=0
		Para i = 0 hasta numero con paso 1 Hacer
			resultado=resultado+i
		FinPara
	FinSi
	Escribir resultado
FinProceso
