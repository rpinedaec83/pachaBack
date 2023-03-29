Proceso ejercicio40
	Definir i, numero1, contador Como Entero
	Definir pi1 Como Real
	pi1 = 0
	contador = 0
	Escribir "Ingrese un número"
	Escribir "Para calcular la sucesión de pi"
	Leer numero1
	Para i=2 Hasta numero1 Con Paso 2 Hacer
		Si (contador mod 2 == 0) Entonces
			pi1 = pi1+(4/(i*(i+1)*(i+2)))
		SiNo
			pi1 = pi1-(4/(i*(i+1)*(i+2)))
		FinSi
		contador = contador+1;
	FinPara
	Escribir "Pi se aproxima a: " pi1 + 3
FinProceso
