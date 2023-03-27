Algoritmo Fibonacci
    Definir n, a, b, c Como Entero
    Escribir("Ingrese el número de términos de la serie que desea calcular:")
    Leer n
    a <- 0
    b <- 1
    Si n = 1 Entonces
        Escribir(a)
    SiNo
        Si n >= 2 Entonces
            Escribir(a)
            Escribir(b)
            Para i = 3 Hasta n Con Paso 1 Hacer
                c <- a + b
                a <- b
                b <- c
                Escribir(c)
            FinPara
        FinSi
    FinSi
FinAlgoritmo
