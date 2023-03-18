Algoritmo Ejercicio20
	//Hacer un algoritmo en Pseint que que lea 4 numeros enteros positivos
	//y verifique y realice las siguientes operaciones:

    //1. ¿Cuantos numeros son Pares?
    //2. ¿Cual es el mayor de todos?

    //3. Si el tercero es par, calcular el cuadrado del segundo.

	//4. Si el primero es menor que el cuarto, calcular
	//la media de los 4 numeros.

	//5. Si el segundo es mayor que el tercero,
	//verificar si el tercero esta comprendido entre los
	//valores 50 y 700. Si cumple se cumple la segunda condicion,
	//calcular la suma de los 4 numeros.

	regla_01 = Falso
	contador_pares = 0
	regla_02 = Verdadero
	numero_mayor = 0
	regla_03 = Falso
	cuadrado_segundo = 0
	regla_04 = Falso
	media = 0
	regla_05 = Falso
	suma_numeros = 0

	Escribir "Ingresa 4 numeros enteros:"

	Escribir "Primer numero: "
	leer n1
	si n1 % 2 == 0 Entonces
		contador_pares = contador_pares + 1
	FinSi
	si n1 > numero_mayor Entonces
		numero_mayor = n1
	FinSi

	Escribir "Segundo numero: "
	leer n2
	si n2 % 2 == 0 Entonces
		contador_pares = contador_pares + 1
	FinSi
	si n2 > numero_mayor Entonces
		numero_mayor = n2
	FinSi

	Escribir "Tercer numero: "
	leer n3
	si n3 % 2 == 0 Entonces
		regla_03 = Verdadero
		contador_pares = contador_pares + 1
		cuadrado_segundo = n2^2
	FinSi
	si n3 > numero_mayor Entonces
		numero_mayor = n3
	FinSi

	Escribir "Cuarto numero: "
	leer n4
	si n4 % 2 == 0 Entonces
		contador_pares = contador_pares + 1
	FinSi
	si n4 > numero_mayor Entonces
		numero_mayor = n4
	FinSi
	si n1 < n4 Entonces
		regla_04 = Verdadero
		media = (n1 + n2 + n3 + n4)/4
	FinSi

	si n2 > n3 Entonces
		si n3 > 50 y n3 < 700 Entonces
			regla_05 = Verdadero
			suma_numeros = (n1 + n2 + n3 + n4)
		FinSi
	FinSi
	si contador_pares <> 0 Entonces
		regla_01 = Verdadero
	FinSi

	si regla_01 = Verdadero Entonces
		Escribir "La cantidad de numeros pares encontrados es : ", contador_pares
	FinSi
	si regla_02 = Verdadero Entonces
		Escribir "El numero mayor es : ", numero_mayor
	FinSi
	si regla_03 = Verdadero Entonces
		Escribir "El cuadrado del segundo numero es : ", cuadrado_segundo
	FinSi
	si regla_04 = Verdadero Entonces
		Escribir "La media aritmetica de los 4 numeros es: ", media
	FinSi
	si regla_05 = Verdadero Entonces
		Escribir "La suma de los 4 numeros es: ", suma_numeros
	FinSi
FinAlgoritmo
