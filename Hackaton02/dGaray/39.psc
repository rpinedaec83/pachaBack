Proceso penultimo
	Definir i,n Como entero	
	Definir pii, denominador Como Real
	Escribir "Ingrese la cantidad de terminoa a utilizar "
	leer n
	pii<-0
	denominador<-1
	Para i<-1 Hasta n Hacer
		pii<-pii+(4/denominador)
		denominador<-denominador+2
		pii<-pii-4/denominador
		denominador<-denominador+2
	Fin Para
	Escribir "La aproximacion de Pi con " n " Terminos es: " pii
FinProceso
