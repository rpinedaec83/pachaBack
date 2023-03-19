Algoritmo ejer5
	//Hacer un algoritmo en Pseint para una tienda de zapatos que tiene una promoción de descuento para vender 
	//al mayor, esta dependerá del número de zapatos que se compren. Si son más de diez, se les dará un 10% de 
	//descuento sobre el total de la compra; si el número de zapatos es mayor de veinte pero menor de treinta, 
	//se le otorga un 20% de descuento; y si son más treinta zapatos se otorgará un 40% de descuento. El precio de cada zapato es de $80.
	//		
	Escribir "ingresa el numero de zapatos"
	leer numzap
	precio=80
	descuento=0
	preciofinal=0
	si numzap> 10 y numzap <=20 Entonces
		descuento=(precio*numzap)*0.1
	SiNo
		si	numzap>20 y numzap<=30 Entonces
			descuento=(precio*numzap)*0.2
		SiNo
			si numzap>30 y numzap <=30 Entonces
				descuento=(precio*numzap)*0.4
			SiNo
				descuento=0
				
			FinSi
		FinSi
		
	FinSi
	preciofinal=(precio*numzap)-descuento
	
	Escribir "tu precio final es ", preciofinal
	
FinAlgoritmo
