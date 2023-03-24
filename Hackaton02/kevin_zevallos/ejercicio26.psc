Algoritmo ejercicio26
	Escribir "Ingrese el dividendo: "
    Leer dividendo 
	Escribir "Ingrese el divisor: "
	Leer divisor
    cociente <- 0
    Mientras dividendo >= divisor Hacer
        dividendo <- dividendo - divisor
        cociente <- cociente + 1
    Fin Mientras
    resto <- dividendo
    Escribir "El cociente es: ", cociente
    Escribir "El resto es: ", resto
FinAlgoritmo