Algoritmo SerieNilakantha
    Definir pii, denominador Como Real
    pii <- 3
    denominador <- 2
    signo <- Verdadero
    Escribir "Ingrese la cantidad de terminos de la serie que desea utilizar:"
    Leer n
    Para i <- 1 Hasta n Hacer
        Si signo Entonces
            pii <- pii + 4 / (denominador * (denominador + 1) * (denominador + 2))
        Sino
            pii <- pii - 4 / (denominador * (denominador + 1) * (denominador + 2))
        FinSi
        denominador <- denominador + 2
        signo <- No signo
    FinPara
    Escribir "El valor aproximado de Pi es:", pii
FinAlgoritmo
