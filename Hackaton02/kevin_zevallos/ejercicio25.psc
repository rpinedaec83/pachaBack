Algoritmo ejercicio25
    Escribir "ingrese un número"
	Leer  n
    factorial <- 1
    i <- 1
    Mientras i <= n Hacer
        factorial <- factorial * i
        i <- i + 1
    Fin Mientras
    Escribir "El factorial de ", n, " es: ", factorial
FinAlgoritmo