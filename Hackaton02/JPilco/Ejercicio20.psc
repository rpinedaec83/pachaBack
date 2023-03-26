//Si el segundo es mayor que el tercero, verificar si el tercero esta comprendido entre los valores 50 y 700. Si cumple se cumple la segunda condición, calcular la suma de los 4 números.
Proceso Ejercicio20
	Definir num1,num2,num3,num4,suma Como Entero
	Escribir "Ingrese el primer numero"
	leer num1
	Escribir "Ingrese el segundo numero"
	leer num2
	Escribir "Ingrese el tercer numero"
	leer num3
	Escribir "Ingrese el cuarto numero"
	leer num4
	
	si num2>num3 Entonces
		si num3>=50 Y num3<=700 Entonces
			suma=num1+num2+num3+num4
			Escribir "La suma de los cuatro numeros es " suma
		SiNo
			Escribir "El tercer numero no cumple la segunda condicion"
		FinSi
	FinSi
	
FinProceso
