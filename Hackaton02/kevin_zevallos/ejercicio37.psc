Algoritmo ejercicio37
	Definir a, b, r Como Entero
    Escribir "Ingrese el primer número:"
    Leer a
    Escribir "Ingrese el segundo número:"
    Leer b
    r <- a mod b
    Mientras r <> 0 Hacer
        a <- b
        b <- r
        r <- a mod b
    Fin Mientras
    Escribir "El máximo común divisor de ", a, " y ", b, " es: ", b


FinAlgoritmo

