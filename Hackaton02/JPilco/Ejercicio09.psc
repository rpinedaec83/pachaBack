//Hacer un algoritmo en Pseint para determinar el aumento de un trabajador, se debe tomar en cuenta que si ganaba más de $2000 tendrá un aumento del 5%, si generaba menos de $2000 su aumento será de un 10%.

Proceso Ejercicio09
	Definir sueldo,aumento Como Real
	Escribir "Ingrese el sueldo del trabajador: "
	leer sueldo
	Si sueldo>2000 Entonces
		aumento=sueldo*0.05
	SiNo
		aumento=sueldo*0.1
	Fin Si
	Escribir "El aumento correspondiente es de $ :" aumento
	
FinProceso
