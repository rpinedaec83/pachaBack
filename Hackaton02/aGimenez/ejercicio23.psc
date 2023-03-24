Proceso ejercicio23
	numero1 = 0 
	suma = 0
	
	Escribir "Ingrese un numero"
	Leer numero1
	
	Para i=1 Hasta numero1 Con Paso 1 Hacer
		si i mod 2<>0 Entonces
			suma = suma + i
		FinSi
	FinPara
	Escribir "Suma de Numeros Impares hasta " numero1 " es " suma
FinProceso
