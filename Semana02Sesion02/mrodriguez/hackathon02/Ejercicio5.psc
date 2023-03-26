Algoritmo Ejercicio5
	//Hacer un algoritmo en Pseint para una tienda de zapatos
	//que tiene una promoci�n de descuento para vender al mayor,
	//esta depender� del n�mero de zapatos que se compren.
	//Si son m�s de diez, se les dar� un 10% de descuento
	//sobre el total de la compra;
	//si el n�mero de zapatos es mayor de veinte
	//pero menor de treinta, se le otorga un 20% de descuento;
	// y si son m�s treinta zapatos se otorgar� un 40% de descuento.
	//El precio de cada zapato es de $80.

	Definir cantidadDeZapatos, descuento Como Entero
	definir precio, precioTotal Como Real

	Escribir "Ingrese la cantidad de zapatos que comprar�"
	Leer cantidadDeZapatos
	precio = 80
	precioTotal=cantidadDeZapatos*precio

	si cantidadDeZapatos > 30 Entonces
		descuento = 40
	SiNo
		si cantidadDeZapatos > 20 Entonces
			descuento = 20
		SiNo
			si cantidadDeZapatos > 10 Entonces
				descuento = 10
			SiNo
				descuento = 0
			FinSi
		FinSi
	FinSi

	precioTotal = precioTotal - (precioTotal * descuento / 100)
	Escribir "El precio total es: S/" , precioTotal
FinAlgoritmo
