Algoritmo MCD_Euclides
    Definir a, b, resto Como Entero
    Escribir "Ingrese el primer número:"
    Leer a
    Escribir "Ingrese el segundo número:"
    Leer b
    Mientras b <> 0 Hacer
        resto <- a Mod b
        a <- b
        b <- resto
    FinMientras
    Escribir "El M.C.D de los números ingresados es: ", a
FinAlgoritmo
