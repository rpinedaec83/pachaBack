Proceso FactorialRecursivo
    Definir n, resultado Como Entero
	
    Escribir "Ingrese un número para calcular su factorial: "
    Leer n
	
    resultado = factorial(n)
	
    Escribir "El factorial de ", n, " es ", resultado
FinProceso

Funcion factorial(num)
    Si num = 0 o num = 1 Entonces
        factorial = 1
    Sino
        factorial = num * factorial(num - 1)
    FinSi
FinFuncion
