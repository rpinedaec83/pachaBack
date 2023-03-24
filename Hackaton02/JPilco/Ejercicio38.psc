//Hacer un algoritmo en Pseint que nos permita saber si un número es un número perfecto.
Proceso Ejercicio38
	Definir numero,suma_divisores Como Entero
	Escribir "Ingrese numero: "
	leer numero
	suma_divisores=0
	para i=1 hasta numero-1 Con Paso 1 Hacer
		Si numero Mod i=0 Entonces
			suma_divisores=suma_divisores+i
		FinSi
	FinPara
	si suma_divisores=numero Entonces
		Escribir numero, " es un numero perfecto. "
	SiNo
		Escribir numero, " no es un numero perfecto. "
		
	FinSi
FinProceso
