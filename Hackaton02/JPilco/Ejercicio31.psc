//Hacer un algoritmo en Pseint parar calcular la media de los números pares e impares, sólo se ingresará diez números.
Proceso Ejercicio31
	para cont=1 Hasta 10 Con Paso 1 Hacer
		Escribir "Ingrese Numero " cont ":"
		leer n
		si	(n mod 2) =0 Entonces
			sumap=sumap+n
		SiNo
			sumai=sumai+n
		FinSi
		sumatotal=sumap+sumai
		mediap=sumap/sumatotal
		mediai=sumai/sumatotal
	FinPara
	Escribir "La media de los pares es: " mediap
	Escribir "La media de los impares es " mediai
	
FinProceso
