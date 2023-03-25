Proceso Fibonacci_serie

    fibonacci=0
	fib1 = 0
	fib2 = 1

    Escribir "Ingrese un número: "
    Leer n
    Escribir "La serie de Fibonacci hasta " n " es:"
	
    Para i = 1 Hasta n Con Paso 1 Hacer
        Escribir(fib1)
        fibonacci = fib1 + fib2
        fib1 = fib2
        fib2 = fibonacci
    FinPara
FinProceso
