Algoritmo ejer40
	//Hacer un algoritmo en Pseint que nos permita saber si un número es un número perfecto.
	Definir numero, sumadivisores Como Entero
    Escribir "Ingrese un número: "
    Leer numero
    sumadivisores <- 0
    Para i <- 1 Hasta (numero - 1) Con Paso 1 Hacer
        Si (numero % i = 0) Entonces
            sumadivisores <- sumadivisores + i
        FinSi
    FinPara
    Si (sumadivisores = numero) Entonces
        Escribir "El número ", numero, " es un número perfecto."
    SiNo
        Escribir "El número ", numero, " no es un número perfecto."
    FinSi
FinAlgoritmo
