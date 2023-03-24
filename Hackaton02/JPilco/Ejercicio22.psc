//Hacer un algoritmo en Pseint para calcular la suma de los n primeros números.
Proceso Ejercicio22
	Definir numero Como Entero
	Escribir "Ingrese el numero a calcular: "
	Leer numero
	Si numero<1 Entonces
		Escribir "El numero ingresado debe ser positivo "
	SiNo
		resultado=0
		Para i=0 hasta numero con paso 1 Hacer
			resultado=resultado+i
		FinPara
	Fin Si
	Escribir " La suma de los n primeros numeros ingresados es" resultado
	
FinProceso
