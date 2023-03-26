Algoritmo ejercicio14
    // Declarar variables
    Definir numero Como Entero
    Definir es_primo Como Logico
	
    // Pedir al usuario que ingrese el número
    Escribir "Ingrese un número del 1 al 10 o el 9: "
    Leer numero
	
    // Comprobar si el número es primo
    Si numero = 1 Entonces
        es_primo <- Falso
    SiNo
        es_primo <- Verdadero
        Para i <- 2 Hasta numero - 1 Con Paso 1 Hacer
            Si numero Mod i = 0 Entonces
                es_primo <- Falso
            FinSi
        FinPara
    FinSi
	
    // Mostrar si el número es primo o no
    Si es_primo Entonces
        Escribir "El número ingresado es primo."
    SiNo
        Escribir "El número ingresado no es primo."
    FinSi
	
FinAlgoritmo

