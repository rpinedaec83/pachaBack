Proceso Ultimo
	Definir n,denominador,pii Como real
	Escribir "Ingrese la cantidad de terminos para la aproximacion de Pii: "
	Leer n
	pii=3.0
	para i=0 hasta n-1 con paso 1 Hacer
		denominador=(2*i+2)*(2*i+3)*(2*i+4)
		Si	i%2=0	Entonces
			pii=pii+4/denominador
		SiNo
			pii=pii-4/denominador
		FinSi
		
	FinPara
	Escribir "El valor aproximado de PI con " n "terminos es: " pii
	
FinProceso
