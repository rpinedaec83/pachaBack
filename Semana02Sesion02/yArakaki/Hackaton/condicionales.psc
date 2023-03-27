Algoritmo condicionales
Escribir "Ingrese el primer número:"
Leer num1

Escribir "Ingrese el segundo número:"
Leer num2

Escribir "Ingrese el tercer número:"
Leer num3

Escribir "Ingrese el cuarto número:"
Leer num4

cant_pares = 0
mayor = num1

Si num1 mod 2 = 0 Entonces
	cant_pares = cant_pares + 1
Fin Si

Si num2 mod 2 = 0 Entonces
	cant_pares = cant_pares + 1
Fin Si

Si num3 mod 2 = 0 Entonces
	cant_pares = cant_pares + 1
Fin Si

Si num4 mod 2 = 0 Entonces
	cant_pares = cant_pares + 1
Fin Si

Si num2 > mayor Entonces
	mayor = num2
Fin Si

Si num3 > mayor Entonces
	mayor = num3
Fin Si

Si num4 > mayor Entonces
	mayor = num4
Fin Si

Si num3 mod 2 = 0 Entonces
	cuadrado_segundo = num2 * num2
	Escribir "El cuadrado del segundo número es:", cuadrado_segundo
Fin Si

Si num1 < num4 Entonces
	media = (num1 + num2 + num3 + num4) / 4
	Escribir "La media de los 4 números es:", media
Fin Si

Si num2 > num3 Entonces
	Si num3 >= 50 Y num3 <= 700 Entonces
		suma = num1 + num2 + num3 + num4
		Escribir "La suma de los 4 números es:", suma
	Fin Si
Fin Si

Escribir "La cantidad de números pares es:", cant_pares
Escribir "El número mayor es:", mayor
FinProceso
